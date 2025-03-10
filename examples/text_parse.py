from pathlib import Path

from datareader.loader import TableLoader
from datareader.parser.text_parser import TextParser

text_table = TextParser(
    Path(__file__).parent / "data" / "text" / "test.txt"
).to_dataframe("|", 3)

print("Loading text table to 'text'...\n", text_table)

TableLoader.load_table("text", text_table)
