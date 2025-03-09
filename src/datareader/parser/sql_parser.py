import re
from typing import Any

from attrs import define, field
from pandas import DataFrame

from .parser_abc import Parser


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


@define
class SQLParser(Parser):
    path: str
    _file: list[str] = field(init=False)

    def __attrs_post_init__(self):
        with open(self.path, encoding="utf-8") as f:
            self._file = f.readlines()

    def to_dataframe(self) -> DataFrame:
        """Parses input SQL Create and Insert statements and constructs a
        Pandas DataFrame.

        Returns:
            A Pandas DataFrame.
        """
        tbl = []
        sql_stmts = " ".join([x.strip("\n") for x in self._file]).split(";")

        for stmt in sql_stmts:
            # How robust is this function to formatting changes?
            # Why is this necessary? Quite messy.
            inside_brackets = _bracket_extract(stmt).replace("(", "").replace(")", "")
            if inside_brackets != "":
                tbl.append(
                    [x.strip() for x in inside_brackets.strip().split(",") if x != ""]
                )

        if len(tbl) == 2:
            tbl = [tbl[0]] + _list_split(tbl[1], len(tbl[0]))

        columns = _get_first_words(tbl[0])

        return DataFrame(tbl[1:], columns=columns)
