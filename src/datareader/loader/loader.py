from attrs import define
from polars import DataFrame

from . import BaseLoader


@define
class Loader:
    _loader: BaseLoader

    def load_table(self, table_name: str, table: DataFrame) -> None:
        """Loads a pandas dataframe object to a postgreSQL database table.

        Args:
            tablename: The name of the table as it will exist in the database.
            table: The pandas dataframe object.

        Returns:
            None
        """
        # Perhaps one glorious day, sqlalchemy will support polars natively.
        table.to_pandas().to_sql(table_name, self._loader.engine(), index=False)
