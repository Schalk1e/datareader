import os


class MissingConfig(Exception):
    """Raised if a required config environment variable is not set."""


# Technically this wouldn't ever return None, but adding return type for mypy.
# If both value and default is None an exception is raised ensuring either value
# or default exists. In the return we prefer returning value, but if value is
# None, then we return default. We'll iron this out in the tests.
def config_from_env(key: str, default: str | None = None) -> str | None:
    """
    Fetches a config value from the global environment, raising
    MissingConfig if it isn't there.
    """
    if not (value := os.environ.get(key, None)) and not default:
        raise MissingConfig(f"{key} not set in the global environment")

    return value if value is not None else default
