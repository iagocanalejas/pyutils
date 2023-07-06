def all_none(*args):
    return all(x is None for x in args)


def all_not_none(*args):
    return all(x is not None for x in args)


def all_or_none(*args):
    return all_none(*args) or all_not_none(*args)

