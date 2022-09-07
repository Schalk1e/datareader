import os

import pandas as pd

from . import Parser


class TextParser(Parser):
    def __init__(self, path: os.PathLike):
        with open(path, "r") as f:
            self._file = f.readlines()

    def to_dataframe(self, delimiter: str, columns: int) -> pd.DataFrame:
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
        df = pd.DataFrame(tbl, columns=headers)
        return df
