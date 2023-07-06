from collections.abc import Iterable, Iterator
from typing import Any


def flatten(xs: Iterable[Any]) -> Iterator[Any]:
    """
    Flatten an iterable of iterables into a single iterable.

    :return: Flattened iterable
    """
    if isinstance(xs, (str, bytes)):
        yield xs
        return

    for x in xs:
        if isinstance(x, Iterable):
            yield from flatten(x)
            continue
        yield x
