from pathlib import Path

from datareader.loader import TableLoader
from datareader.parser.sql_parser import SQLParser

single_insert = SQLParser(
    Path(__file__).parent / "data" / "sql" / "single_insert.sql"
).to_dataframe()

print("Uploading table 'single_insert'...\n", single_insert)

TableLoader.load_table("single_insert", single_insert)

multiple_insert = SQLParser(
    Path(__file__).parent / "data" / "sql" / "multiple_insert.sql"
).to_dataframe()

print("Uploading table 'multiple_insert'...\n", multiple_insert)

TableLoader.load_table("multiple_insert", multiple_insert)
