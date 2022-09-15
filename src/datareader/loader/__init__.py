import os

from sqlalchemy import create_engine


class ConfigMissingError(Exception):
    pass


try:
    USER = os.environ["DATAREADER_DB_USERNAME"]
    PASSWORD = os.environ["DATAREADER_DB_PASSWORD"]
    DATABASE = os.environ["DATAREADER_DB_NAME"]
except KeyError as e:
    raise ConfigMissingError(
        "A configuration parameter is missing from the environment (Database user, password or db name). Please ensure these are defined!"
    )

try:
    PORT = os.environ["DATAREADER_DB_PORT"]
except KeyError as e:
    print(
        "Setting port to default pgsql port 5432. If this is not the correct port, add DATAREADER_DB_PORT to the environment variables."
    )
    PORT = 5432

try:
    HOST = os.environ["DATAREADER_DB_HOST"]
except KeyError as e:
    print(
        "Setting host to localhost. If this is not the correct host, add DATAREADER_DB_HOST to the environment variables."
    )
    HOST = "localhost"

if not all(USER, PASSWORD, DATABASE):
    raise ConfigMissingError(
        "A configuration parameter is missing from the environment (Database user, password or db name). Please ensure these are defined!"
    )


class BaseLoader:
    def __init__(self, user, password, host, database, port) -> None:
        self._connect_str = (
            f"postgresq;://{user}:{password}@{host}@{port}/{database}"
        )

    def engine(self):
        return create_engine(self._connect_str)


loader = BaseLoader(USER, PASSWORD, HOST, DATABASE, PORT)

from .main import TableLoader
