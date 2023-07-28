from typing import Generator, Iterable, TypeVar


T = TypeVar("T")


def flatten(xs: Iterable[T | Iterable[T]]) -> Generator[T, None, None]:
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x
