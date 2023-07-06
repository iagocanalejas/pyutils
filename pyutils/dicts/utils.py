from typing import Any

from pyutils.strings.transformers import camel_to_snake


def camel_to_snake_dict(camel_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Converts a dictionary's keys from camel case to snake case.

    :param camel_dict: dictionary with camel case keys
    :return: dictionary with snake case keys
    """
    snake_dict: dict[str, Any] = {}
    for k, v in camel_dict.items():
        new_key = camel_to_snake(k)
        if isinstance(v, dict):
            snake_dict[new_key] = camel_to_snake_dict(v)
        elif isinstance(v, list):
            snake_dict[new_key] = [camel_to_snake_dict(i) if isinstance(i, dict) else i for i in v]
        else:
            snake_dict[new_key] = v
    return snake_dict


def copy_dict(d: dict[str, Any], exclude: list[str] | None = None) -> dict[str, Any]:
    """
    :param d: valid dictionary
    :param exclude: keys to exclude
    :return: A copy of the given dict without excluded keys
    """
    if exclude is None:
        exclude = []
    return {k: v for k, v in d.items() if k not in exclude}


def clean_dict(d: dict[Any, Any]) -> dict[Any, Any]:
    """
    :param d: valid dictionary
    :return: A copy of the given dict without None values
    """
    return {k: v for k, v in d.items() if v is not None}
