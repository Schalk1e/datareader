import os

from pandas import DataFrame

from . import Parser
from attrs import define, field

from typing import Iterator


@define
class TextParser(Parser):
    path: os.PathLike
    _file: str = field(init=False)

    def __attrs_post_init__(self):
        with open(self.path) as f:
            self._file = f.readlines()

    def to_dataframe(self, delimiter: str, columns: int) -> DataFrame:
        """Parses input text table and constructs a Pandas DataFrame.

        Returns:
            A Pandas DataFrame.
        """
        rows = [line.split(delimiter) for line in self._file]

        tbl = []
        for row in rows:
            r = [r.strip() for r in row if r.strip() != ""]
            if len(r) == columns:
                tbl.append(r)

        headers = tbl.pop(0)

        return DataFrame(tbl, columns=headers)
