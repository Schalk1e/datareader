from pandas.testing import assert_frame_equal

import os
from datareader.parser.text_parser import TextParser

import pytest
from pathlib import Path

sqldir = Path(__file__).parent / "data" / "text"


@pytest.mark.parametrize("file", os.listdir(sqldir))
def test_text_parser_dataframe_result(file, text_parser_dataframe_result):
    parser = TextParser(path=os.path.join(sqldir, file))

    assert_frame_equal(parser.to_dataframe("|", 3), text_parser_dataframe_result)
