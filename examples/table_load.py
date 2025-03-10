from pandas import DataFrame

from datareader.loader import TableLoader

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

TableLoader.load_table("test", df)
