import os
from pathlib import Path

import pytest
from pandas.testing import assert_frame_equal

from datareader.parser.sql_parser import SQLParser

sqldir = Path(__file__).parent / "data" / "sql"


@pytest.mark.parametrize("file", os.listdir(sqldir))
def test_sql_parser_dataframe_result(file, sql_parser_dataframe_result):
    path = sqldir / file
    parser = SQLParser(path)

    assert_frame_equal(parser.to_dataframe(), sql_parser_dataframe_result)
