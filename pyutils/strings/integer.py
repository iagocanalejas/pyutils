def int_or_none(v: str) -> int | None:
    """
    :return: integer value or None if it's not an integer
    """
    try:
        return int(v)
    except ValueError:
        return None
