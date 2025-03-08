from pandas.testing import assert_frame_equal

import os
from datareader.parser.sql_parser import SQLParser

import pytest
from pathlib import Path

sqldir = Path(__file__).parent / "data" / "sql"


@pytest.mark.parametrize("file", os.listdir(sqldir))
def test_sql_parser_dataframe_result(file, sql_parser_dataframe_result):
    parser = SQLParser(path=os.path.join(sqldir, file))

    assert_frame_equal(parser.to_dataframe(), sql_parser_dataframe_result)
