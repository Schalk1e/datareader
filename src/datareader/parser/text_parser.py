from pathlib import Path

from attrs import define, field
from polars import DataFrame

from datareader.helpers import _build_df_dict

from .parser_abc import Parser


@define
class TextParser(Parser):
    path: Path
    _file: list[str] = field(init=False)

    def __attrs_post_init__(self):
        with open(self.path) as f:
            self._file = f.readlines()

    def to_dataframe(self, delimiter: str, columns: int) -> DataFrame:
        """Parses input text table and constructs a Pandas DataFrame.

        Returns:
            A Pandas DataFrame.
        """
        rows = (line.split(delimiter) for line in self._file)
        tbl = [
            r
            for row in rows
            # Can use filter here, but the list comp feels more readable than
            #  if len(r := list(filter(None, (x.strip() for x in row)))) == columns
            if len(r := [x.strip() for x in row if x.strip()]) == columns
        ]
        headers = tbl.pop(0)

        return DataFrame(_build_df_dict(tbl, headers=headers))
