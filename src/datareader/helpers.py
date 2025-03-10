from typing import Any


def _build_df_dict(rows: list[list[Any]], headers: list[str]) -> dict[str, list[Any]]:
    """
    Convert a list of rows and a list of headings into a dict that can
    be passed to polars.DataFrame.
    """
    return {header: [row[idx] for row in rows] for idx, header in enumerate(headers)}
