from datareader.parser.sql_parser import (
    extract_bracket,
    first_words,
    split_list,
)


def test_extract_bracket(test_extract_bracket_cases):
    for case in test_extract_bracket_cases:
        assert extract_bracket(case.input_value) == case.output_value


def test_first_words(test_first_words_cases):
    for case in test_first_words_cases:
        assert first_words(case.input_value) == case.output_value


def test_split_list(test_split_list_cases):
    for case in test_split_list_cases:
        assert split_list(case.input_value[0], case.input_value[1]) == case.output_value
