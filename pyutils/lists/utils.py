from collections.abc import Iterable
from typing import Any

IterableAny = Iterable[Any | Iterable["IterableAny"]]


def flatten(xs: IterableAny) -> Iterable[Any]:
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
