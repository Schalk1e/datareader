import os
from abc import ABC, abstractmethod

import pandas as pd


class Parser(ABC):
    @abstractmethod
    def __init__(self, infile: os.PathLike) -> None:
        pass

    @abstractmethod
    def to_dataframe(self) -> pd.DataFrame:
        pass
