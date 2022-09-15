from test_cases.sql_parser_cases import (
    extract_bracket_cases,
    first_words_cases,
    split_list_cases,
)

from datareader.sql_parser import extract_bracket, first_words, split_list


def test_extract_bracket():
    test_cases = extract_bracket_cases()
    for case, result in zip(test_cases["cases"], test_cases["results"]):
        assert extract_bracket(case) == result


def test_split_list():
    test_cases = split_list_cases()
    for case, result in zip(test_cases["cases"], test_cases["results"]):
        assert split_list(case[0], case[1]) == result


def test_first_words():
    test_cases = first_words_cases()
    for case, result in zip(test_cases["cases"], test_cases["results"]):
        assert first_words(case) == result
