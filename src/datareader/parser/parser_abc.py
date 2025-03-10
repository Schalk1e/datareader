from abc import ABC, abstractmethod

from polars import DataFrame


class Parser(ABC):
    @abstractmethod
    def to_dataframe(self, *kwargs) -> DataFrame:
        pass
