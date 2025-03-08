from attrs import define, field
import os
import re

import pandas as pd

from . import Parser


def extract_bracket(input_string: str) -> str:
    """Extracts text between (outermost) brackets rounded brackets.

    Args:
        input_string: The string to search over.

    Returns:
        The text within the outermost brackets.
    """
    if input_string == "":
        return input_string
    match_object = re.search(r"\((.*)\)", input_string)
    if match_object:
        return match_object.group(1)
    return ""


def split_list(input_string: list, n: int) -> list:
    """Splits an input list into individual lists of size n and remainder.

    Args:
        input_string: The string to search over.
        n: Split size.

    Returns:
        A list of split lists.
    """
    iterations = len(input_string) // n
    splitlist = []
    i = 0
    while i < iterations:
        to_append = input_string[n * i : n * (i + 1)]
        if to_append:
            splitlist.append(to_append)
        i += 1
    dmod = len(input_string) % n
    if dmod != 0:
        splitlist.append(input_string[-dmod:])
    return splitlist


def first_words(input_list: list) -> list:
    """Finds the first words delimited with a space in a list of strings.

    Args:
        input_list: List of strings.

    Returns:
        A list of strings containing the first words in each input string.
    """
    return [x.strip().split(" ")[0] for x in input_list]


@define
class SQLParser(Parser):
    path: os.PathLike
    _file: str = field(init=False)

    def __attrs_post_init__(self):
        with open(self.path, "r", encoding="utf-8") as f:
            self._file = f.readlines()

    def to_dataframe(self) -> pd.DataFrame:
        """Parses input SQL Create and Insert statements and constructs a Pandas DataFrame.

        Returns:
            A Pandas DataFrame.
        """
        # add unique constraint option.
        tbl = []
        q = " ".join([x.strip("\n") for x in self._file]).split(";")
        for x in q:
            b = extract_bracket(x).replace("(", "").replace(")", "")
            if b != "":
                to_append = b.strip().split(",")
                tbl.append([y.strip() for y in to_append if y != ""])
        if len(tbl) == 2:
            tbl = [tbl[0]] + split_list(tbl[1], len(tbl[0]))
        cols = first_words(tbl[0])
        df = pd.DataFrame(tbl[1:], columns=cols)
        return df
