import os
import re

import pandas as pd

from . import Parser


def extract_bracket(s: str) -> str:
    if s == "":
        return s
    return re.search("\((.*)\)", s).group(1).replace("(", "").replace(")", "")


def split_list(s: list, n: int) -> list:
    iterations = len(s) // n
    splitlist = []
    i = 0
    while i < iterations:
        to_append = s[n * i : n * (i + 1)]
        if to_append:
            splitlist.append(to_append)
        i += 1
    dmod = len(s) % n
    if dmod != 0:
        splitlist.append(s[-dmod:])
    return splitlist


def first_words(input: list) -> list:
    return [x.strip().split(" ")[0] for x in input]


class SQLParser(Parser):
    def __init__(self, path: os.PathLike):
        with open(path, "r") as f:
            self._file = f.readlines()

    def to_dataframe(self):
        tbl = []
        q = " ".join([x.strip("\n") for x in self._file]).split(";")
        for x in q:
            b = extract_bracket(x)
            if b != "":
                tbl.append(b.strip().split(","))
        if len(tbl) == 2:
            tbl = [tbl[0]] + split_list(tbl[1], len(tbl[0]))
        cols = first_words(tbl[0])
        df = pd.DataFrame(tbl[1:], columns=cols)
        return df
