from sqlalchemy import create_engine

from .config import config_from_env

USER = config_from_env("USER")
PASSWORD = config_from_env("PASSWORD")
DATABASE = config_from_env("DATABASE")
PORT = config_from_env("PORT", default="5432")
HOST = config_from_env("HOST", default="localhost")


class BaseLoader:
    def __init__(self, user, password, host, database, port) -> None:
        self._connect_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"

    def engine(self):
        return create_engine(self._connect_str)


base_loader: BaseLoader = BaseLoader(USER, PASSWORD, HOST, DATABASE, PORT)

from .main import TableLoader as TableLoader
