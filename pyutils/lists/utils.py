from typing import Generator, Iterable, List, TypeVar

T = TypeVar("T")


def flatten(xs: Iterable[T | Iterable[T]]) -> Generator[T, None, None]:
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def chunk(input_list: List[T], chunk_size: int) -> List[List[T]]:
    return [input_list[i : i + chunk_size] for i in range(0, len(input_list), chunk_size)]
