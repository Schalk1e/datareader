import os
from abc import ABC, abstractmethod

import pandas as pd


class Parser(ABC):
    @abstractmethod
    def to_dataframe(self) -> pd.DataFrame:
        pass
