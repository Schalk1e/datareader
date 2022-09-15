import os

import pandas as pd

from . import Tests


def extract_bracket_cases():
    return {
        "cases": [
            "(s)",
            "( s )",
            "((s))",
            "((s)",
            "(s",
            "s)",
            "(((((s)))))",
            "s",
            "",
        ],
        "results": ["s", " s ", "(s)", "(s", "", "", "((((s))))", "", ""],
    }


def split_list_cases():
    return {
        "cases": [
            ([1, 2, 3, 4], 1),
            ([1, 2, 3, 4], 2),
            ([1, 2, 3, 4], 3),
            ([1, 2, 3, 4], 4),
            ([1, 2, 3, 4], 5),
            ([1], 1),
            ([1], 2),
        ],
        "results": [
            [[1], [2], [3], [4]],
            [[1, 2], [3, 4]],
            [[1, 2, 3], [4]],
            [[1, 2, 3, 4]],
            [[1, 2, 3, 4]],
            [[1]],
            [[1]],
        ],
    }


def first_words_cases():
    return {
        "cases": [
            ["a b", "b c", "c d"],
            ["a b"],
            ["a"],
            [""],
            ["a b c"],
            ["a b c", "b c d"],
            ["abc"],
            [],
        ],
        "results": [
            ["a", "b", "c"],
            ["a"],
            ["a"],
            [""],
            ["a"],
            ["a", "b"],
            ["abc"],
            [],
        ],
    }


class ParserTestCases(Tests):
    def __init__(self, path: os.PathLike):
        self._path = path
        self._files = []
        for file in os.listdir(path):
            self._files.append(os.path.join(os.getcwd(), path, file))

    def to_dataframe_cases(self):
        return {
            "cases": self._files,
            "results": len(self._files)
            * [
                pd.DataFrame(
                    {"name": ["'John'", "'Lyla'"], "year": ["2003", "1994"]}
                ),
            ],
        }
