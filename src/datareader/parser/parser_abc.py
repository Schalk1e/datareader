from abc import ABC, abstractmethod

import pandas as pd


class Parser(ABC):
    @abstractmethod
    def to_dataframe(self, *kwargs) -> pd.DataFrame:
        pass
