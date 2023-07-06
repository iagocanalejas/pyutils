from collections.abc import Iterable, Mapping

type Nested[T] = T | Iterable[Nested[T]]


def flatten[T](xs: Iterable[Nested[T]]) -> Iterable[T]:
    """
    Flatten an iterable of iterables into a single iterable.

    :return: Flattened iterable
    """
    if isinstance(xs, (str, bytes, Mapping)):
        yield xs  # type: ignore[misc]
        return

    for x in xs:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x
