from test_cases.text_parser_cases import TextTestCases

from datareader.parser import text_parser


# def test_to_dataframe():
#     test_cases = TextTestCases("tests/test_cases/data/text/").to_dataframe_cases()
#     for case, result in zip(test_cases["cases"], test_cases["results"], strict=False):
#         assert (
#             text_parser.TextParser(case)
#             .to_dataframe("|", 3)
#             .astype(str)
#             .equals(result.astype(str))
#         )
