from pandas import DataFrame


class Loader:
    def __init__(self, loader) -> None:
        self._loader = loader

    def load_table(self, table_name: str, table: DataFrame) -> None:
        """Loads a pandas dataframe object to a postgreSQL database table.

        Args:
            tablename: The name of the table as it will exist in the database.
            table: The pandas dataframe object.

        Returns:
            None
        """
        table.to_sql(table_name, self._loader.engine())
