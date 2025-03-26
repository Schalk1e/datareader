import re
from pathlib import Path
from typing import Any

from attrs import define, field
from polars import DataFrame

from datareader.helpers import _build_df_dict

from .parser_abc import Parser


@define
class SQLParser(Parser):
    path: Path
    _file: list[str] = field(init=False)

    def __attrs_post_init__(self):
        with open(self.path, encoding="utf-8") as f:
            self._file = f.readlines()

    def to_dataframe(self, columns: int) -> DataFrame:
        """Parses input SQL Create and Insert statements and constructs a
        Pandas DataFrame.

        Returns:
            A Pandas DataFrame.
        """
        sql_stmts = " ".join(x.strip() for x in self._file).split(";")

        # We're planning on iterating over this in tbl. No need to store
        # can use generator exp.
        inside_brackets = (
            _bracket_extract(x).translate(str.maketrans("", "", "()"))
            for x in sql_stmts
        )

        tbl_data = [
            item
            for stmt in inside_brackets
            # Filter out any "" which we sometimes get. Ensure whitespace is
            # stripped from each split (on ,) stmt.
            for item in filter(None, (x.strip() for x in stmt.split(",")))
        ]

        tbl = [tbl_data[:columns], *_list_split(tbl_data[columns:], columns)]
        headers = _get_first_words(tbl[0])

        # First list element is the header list.
        # _build_df_dict takes data and headers separately.
        return DataFrame(_build_df_dict(tbl[1:], headers=headers))


def _bracket_extract(input_string: str) -> str:
    """Extracts text between (outermost) brackets rounded brackets.

    Args:
        input_string: The string to search over.

    Returns:
        The text within the outermost brackets.
    """
    match_object = re.search(r"\((.*)\)", input_string)
    if match_object:
        return match_object.group(1)
    return ""


def _list_split(input_list: list[Any], n: int) -> list[Any]:
    """Splits an input list into individual lists of size n and remainder.

    Args:
        input_string: The string to search over.
        n: Split size.

    Returns:
        A list of split lists.
    """
    return [input_list[i : i + n] for i in range(0, len(input_list), n)]


def _get_first_words(input_list: list[str]) -> list[str]:
    """Finds the first words delimited with a space in a list of strings.

    Args:
        input_list: List of strings.

    Returns:
        A list of strings containing the first words in each input string.
    """
    return [x.strip().split(" ")[0] for x in input_list]
