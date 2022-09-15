import os
from abc import ABC, abstractmethod


class Tests(ABC):
    @abstractmethod
    def __init__(self, infile: os.PathLike):
        pass

    @abstractmethod
    def to_dataframe_cases(self) -> dict:
        pass
