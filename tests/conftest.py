import os
from dataclasses import dataclass
from typing import Any
from unittest import mock

import pytest
from polars import DataFrame

# We look for some env vars on import. Let's set them for now and come back to
# this later.
os.environ["DATAREADER_PG_USER"] = "TEST_USER"
os.environ["DATAREADER_PG_PASSWORD"] = "TEST_PASS"  # noqa
os.environ["DATAREADER_PG_DATABASE"] = "TEST_DB"


@dataclass
class BracketTestCase:
    input_value: str
    output_value: str


@dataclass
class SplitListTestCase:
    input_value: tuple[list[int], int]
    output_value: list[list[int]]


@dataclass
class FirstWordsTestCase:
    input_value: list[str]
    output_value: list[str]


@dataclass
class BuildDictTestCase:
    input_value: tuple[list[list[Any]], list[str]]
    output_value: dict[str, list[Any]]


@pytest.fixture
def test_bracket_extract_cases():
    return [
        BracketTestCase(input_value="(s)", output_value="s"),
        BracketTestCase(input_value="( s )", output_value=" s "),
        BracketTestCase(input_value="((s))", output_value="(s)"),
        BracketTestCase(input_value="((s)", output_value="(s"),
        BracketTestCase(input_value="(s", output_value=""),
        BracketTestCase(input_value="s)", output_value=""),
        BracketTestCase(input_value="(((((s)))))", output_value="((((s))))"),
        BracketTestCase(input_value="s", output_value=""),
        BracketTestCase(input_value="", output_value=""),
    ]


@pytest.fixture
def test_list_split_cases():
    return [
        SplitListTestCase(
            input_value=([1, 2, 3, 4], 1), output_value=[[1], [2], [3], [4]]
        ),
        SplitListTestCase(input_value=([1, 2, 3, 4], 2), output_value=[[1, 2], [3, 4]]),
        SplitListTestCase(input_value=([1, 2, 3, 4], 3), output_value=[[1, 2, 3], [4]]),
        SplitListTestCase(input_value=([1, 2, 3, 4], 4), output_value=[[1, 2, 3, 4]]),
        SplitListTestCase(input_value=([1, 2, 3, 4], 5), output_value=[[1, 2, 3, 4]]),
        SplitListTestCase(input_value=([1], 1), output_value=[[1]]),
        SplitListTestCase(input_value=([1], 2), output_value=[[1]]),
    ]


@pytest.fixture
def test_get_first_words_cases():
    return [
        FirstWordsTestCase(
            input_value=["a b", "b c", "c d"], output_value=["a", "b", "c"]
        ),
        FirstWordsTestCase(input_value=["a b"], output_value=["a"]),
        FirstWordsTestCase(input_value=["a"], output_value=["a"]),
        FirstWordsTestCase(input_value=[""], output_value=[""]),
        FirstWordsTestCase(input_value=["a b c"], output_value=["a"]),
        FirstWordsTestCase(input_value=["a b c", "b c d"], output_value=["a", "b"]),
        FirstWordsTestCase(input_value=["abc"], output_value=["abc"]),
    ]


@pytest.fixture
def test_build_df_dict_cases():
    return [
        BuildDictTestCase(
            input_value=([[1, 2, 3], [1, 2, 3]], ["a", "b", "c"]),
            output_value={"a": [1, 1], "b": [2, 2], "c": [3, 3]},
        ),
    ]


@pytest.fixture
def sql_parser_dataframe_result():
    return DataFrame({"name": ["'John'", "'Lyla'"], "year": ["2003", "1994"]})


@pytest.fixture
def text_parser_dataframe_result():
    return DataFrame(
        {
            "a": ["1", "1"],
            "b": ["2", "2"],
            "c": ["3", "3"],
        }
    )


@pytest.fixture()
def setenvvar(monkeypatch):
    with mock.patch.dict(os.environ, clear=True):
        envvars = {
            "TEST_STRING": "test_string",
        }
        for k, v in envvars.items():
            monkeypatch.setenv(k, v)
        yield
