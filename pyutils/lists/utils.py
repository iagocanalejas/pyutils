from collections.abc import Generator, Iterable
from typing import Any


def flatten(xs: Iterable[Any | Iterable[Any]]) -> Generator[Any, None, None]:
    """
    Flatten an iterable of iterables into a single iterable.

    :return: Flattened iterable
    """
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x
