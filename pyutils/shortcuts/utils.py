import uuid


def generate_unique_code(length: int = 8) -> str:
    """
    :return: Generated 'length' length hexadecimal number
    """
    return uuid.uuid4().hex[:length].upper()


def copy[T](d: dict[str, T], exclude: list[str] | None = None) -> dict[str, T]:
    """
    :param d: valid dictionary
    :param exclude: keys to exclude
    :return: A copy of the given dict without excluded keys
    """
    if exclude is None:
        exclude = []
    return {k: v for k, v in d.items() if k not in exclude}


def clean_dict(d: dict) -> dict:
    """
    :param d: valid dictionary
    :return: A copy of the given dict without None values
    """
    return {k: v for k, v in d.items() if v is not None}
