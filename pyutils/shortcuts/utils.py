from typing import Any, Dict, List, Optional
import uuid


def generate_unique_code(length: int = 8) -> str:
    """
    :return: Generated 'length' length hexadecimal number
    """
    return uuid.uuid4().hex[:length].upper()


def copy(d: Dict[str, Any], exclude: Optional[List[str]] = None):
    """
    :param d: valid dictionary
    :param exclude: keys to exclude
    :return: A copy of the given dict without excluded keys
    """
    if exclude is None:
        exclude = []
    return {k: v for k, v in d.items() if k not in exclude}

