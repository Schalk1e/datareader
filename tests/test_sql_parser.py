from test_cases.sql_parser_cases import ParserTestCases

from datareader.sql_parser import SQLParser


def test_to_dataframe():
    test_cases = ParserTestCases(
        "tests/test_cases/data/sql/"
    ).to_dataframe_cases()
    for case, result in zip(test_cases["cases"], test_cases["results"]):
        assert (
            SQLParser(case)
            .to_dataframe()
            .astype(str)
            .equals(result.astype(str))
        )
