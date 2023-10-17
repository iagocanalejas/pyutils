from typing import Any, Generator, Iterable


def flatten(xs: Iterable[Any | Iterable[Any]]) -> Generator[Any, None, None]:
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x
