from typing import Any

import pytest

from pyutils.lists import flatten


@pytest.mark.parametrize(
    ("v", "result"),
    [
        ([], []),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([1, [2, [3, 4, [], [1, 2]]], 5], [1, 2, 3, 4, 1, 2, 5]),
        (["asdf"], ["asdf"]),
        (
            ["asdf", ["qwer", ["zxcv", "uiop", [], ["jkl;", ["bnm,"]]]], "qwer"],
            ["asdf", "qwer", "zxcv", "uiop", "jkl;", "bnm,", "qwer"],
        ),
    ],
)
def test_flatten(v: list[Any], result: list[Any]) -> None:
    assert list(flatten(v)) == result
