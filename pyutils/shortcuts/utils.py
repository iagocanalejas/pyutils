import uuid
from typing import Any


def generate_unique_code(length: int = 8) -> str:
    """
    :return: Generated 'length' length hexadecimal number
    """
    return uuid.uuid4().hex[:length].upper()


def copy(d: dict[str, Any], exclude: list[str] | None = None):
    """
    :param d: valid dictionary
    :param exclude: keys to exclude
    :return: A copy of the given dict without excluded keys
    """
    if exclude is None:
        exclude = []
    return {k: v for k, v in d.items() if k not in exclude}
