from datareader.parser.sql_parser import (
    _bracket_extract,
    _get_first_words,
    _list_split,
)


def test__bracket_extract(test_bracket_extract_cases):
    for case in test_bracket_extract_cases:
        assert _bracket_extract(case.input_value) == case.output_value


def test_first_words(test_get_first_words_cases):
    for case in test_get_first_words_cases:
        assert _get_first_words(case.input_value) == case.output_value


def test_split_list(test_list_split_cases):
    for case in test_list_split_cases:
        assert (
            _list_split(case.input_value[0], case.input_value[1]) == case.output_value
        )
