from datareader.parser.sql_parser import (
    SQLParser,
    extract_bracket,
    split_list,
    first_words,
)

# def test_to_dataframe(test_to_dataframe_cases):
#     for case in test_to_dataframe_cases:
#         assert (
#             SQLParser(case.input_value).to_dataframe().astype(str) == case.output_value
#         )
