from dataclasses import dataclass

import pytest
from pandas import DataFrame


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
