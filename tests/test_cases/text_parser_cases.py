import os

import pandas as pd

from . import Tests


class TextTestCases(Tests):
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
                    {
                        "a": ["1", "1"],
                        "b": ["2", "2"],
                        "c": ["3", "3"],
                    }
                ),
            ],
        }
