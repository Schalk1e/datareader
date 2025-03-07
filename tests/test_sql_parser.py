from test_cases.sql_parser_cases import ParserTestCases

from datareader.parser import sql_parser


def test_to_dataframe():
    test_cases = ParserTestCases("tests/test_cases/data/sql/").to_dataframe_cases()
    for case, result in zip(test_cases["cases"], test_cases["results"], strict=False):
        assert (
            sql_parser.SQLParser(case)
            .to_dataframe()
            .astype(str)
            .equals(result.astype(str))
        )
