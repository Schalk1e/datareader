from pandas import DataFrame


class Loader:
    def __init__(self, loader, table: DataFrame) -> None:
        self._loader = loader
        self._table = table

    def load_table(self, table_name: str) -> None:
        self._table.to_sql(table_name, self._loader.engine())
