from collections.abc import Iterable
from typing import Any

IterableAny = Iterable[Any | Iterable["IterableAny"]]


def flatten(xs: IterableAny) -> Iterable[Any]:
    """
    Flatten an iterable of iterables into a single iterable.
    :return: Flattened iterable
    """
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x
