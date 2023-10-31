def all_none(*args) -> bool:
    """
    :return: True if all arguments are None
    """
    return all(x is None for x in args)


def all_not_none(*args) -> bool:
    """
    :return: True if all arguments are not None
    """
    return all(x is not None for x in args)


def all_or_none(*args) -> bool:
    """
    :return: True if all arguments are None or all are not None
    """
    return all_none(*args) or all_not_none(*args)


def only_one_not_none(*args) -> bool:
    """
    :return: True if only one argument is not None
    """
    return sum(x is not None for x in args) == 1
