from pandas import DataFrame


class Loader:
    def __init__(self, loader) -> None:
        self._loader = loader

    def load_table(self, table_name: str, table: DataFrame) -> None:
        table.to_sql(table_name, self._loader.engine())
