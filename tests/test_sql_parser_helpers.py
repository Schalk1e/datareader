from datareader.parser.sql_parser import (
    extract_bracket,
    first_words,
    split_list,
)

import pytest
from dataclasses import dataclass


@dataclass
class TestCase:
    input_value: str
    output_value: str


@pytest.fixture
def test_extract_bracket_cases():
    return [
        TestCase(input_value="(s)", output_value="s"),
        TestCase(input_value="( s )", output_value=" s "),
        TestCase(input_value="((s))", output_value="(s)"),
        TestCase(input_value="((s)", output_value="(s"),
        TestCase(input_value="(s", output_value=""),
        TestCase(input_value="s)", output_value=""),
        TestCase(input_value="(((((s)))))", output_value="((((s))))"),
        TestCase(input_value="s", output_value=""),
        TestCase(input_value="", output_value=""),
    ]


@pytest.fixture
def test_first_words_cases():
    return []


@pytest.fixture
def test_split_list_cases():
    return []


def test_extract_bracket(test_extract_bracket_cases):
    for case in test_extract_bracket_cases:
        assert extract_bracket(case.input_value) == case.output_value


def test_first_words():
    assert True


def test_split_list():
    assert True
