<h1 align="center">
  :octocat: datareader
</h1>

<div align="center">
  <p>
    <img src="https://github.com/Schalk1e/datareader/workflows/lint/badge.svg" width="120" />
  </p>
</div>

A simple package to read input data from text into a Python session or PostgreSQL DB. Functionality like this exists elsewhere but I wanted my own, in one place, to make coding assignments and interviews easier :)

# usage

## parsing sql

To read a SQL create and insert statement from a text file, parse it and create a Python DataFrame, use the following.

```
from datareader.parser import sql_parser

df = sql_parser.SQLParser("path/to/file/file.txt").to_dataframe()
```

This expects a SQL create and insert statement following the convention shown under `tests/test_cases/data/sql/`. Validation logic is incoming!

## parsing text

To read a text table with arbitrary delimiters and row dividers, use the following. 

```
from datareader.parser import text_parser

delimiter = "|"
columns = 3
df = text_parser.TextParser("path/to/file/file.txt").to_dataframe(delimiter, columns)
```

## loading data

To load data from a dataframe into a postgreSQL table, all the required variables are read from the environment upon instantiation of the `TableLoader` class. 

```
export "DATAREADER_DB_USERNAME"=<>
export "DATAREADER_DB_PASSWORD"=<>
export "DATAREADER_DB_NAME"=<>
# Optional 
export "DATAREADER_DB_HOST"=<> # Defaults to localhost.
export "DATAREADER_DB_PORT"=<> # Defaults to 5432.
```

In session.

```
from datareader.loader import TableLoader

df = pd.DataFrame({'a' : [1,2,3], 'b' : [1,2,3]})


tl = TableLoader()
"""
This will write a table named 'test' to the database.
tl.load_table("test", df)
"""
```

