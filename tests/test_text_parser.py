import os
from pathlib import Path

import pytest
from pandas.testing import assert_frame_equal

from datareader.parser.text_parser import TextParser

sqldir = Path(__file__).parent / "data" / "text"


@pytest.mark.parametrize("file", os.listdir(sqldir))
def test_text_parser_dataframe_result(file, text_parser_dataframe_result):
    path = sqldir / file
    parser = TextParser(path)

    assert_frame_equal(parser.to_dataframe("|", 3), text_parser_dataframe_result)
