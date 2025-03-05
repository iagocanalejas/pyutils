from typing import Any

from pyutils.strings.transformers import camel_to_snake


def camel_to_snake_dict(camel_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Converts a dictionary's keys from camel case to snake case. This version
    handles nested dictionaries and lists.
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
