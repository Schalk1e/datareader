from pytest import raises

from datareader.loader.config import MissingConfig, config_from_env


def test_config_from_env_without_default(setenvvar):
    """
    Does the config_from_env method retrieve an existing string env var
    correctly?

    """
    test_env_var = config_from_env("TEST_STRING")

    assert test_env_var == "test_string"
    assert isinstance(test_env_var, str)


def test_config_from_env_with_default(setenvvar):
    """
    Does the config_from_env method retrieve an existing string env var
    correctly?

    """
    test_env_var = config_from_env("TEST", default="test_string")

    assert test_env_var == "test_string"
    assert isinstance(test_env_var, str)


def test_config_from_env_no_var_no_default(setenvvar):
    """
    Does the config_from_env method retrieve an existing string env var
    correctly?

    """
    with raises(MissingConfig) as excinfo:
        config_from_env("TEST")

    assert str(excinfo.value) == "TEST not set in the global environment"
