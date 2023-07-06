import unittest

from pyutils.lists import flatten


class TestLists(unittest.TestCase):
    def test_flatten(self) -> None:
        results = [
            ([], []),
            ([1, 2, 3, 4], [1, 2, 3, 4]),
            ([1, [2, 3], 4], [1, 2, 3, 4]),
            ([1, [2, [3, 4, [], [1, 2]]], 5], [1, 2, 3, 4, 1, 2, 5]),
            (["asdf"], ["asdf"]),
            (
                ["asdf", ["qwer", ["zxcv", "uiop", [], ["jkl;", ["bnm,"]]]], "qwer"],
                ["asdf", "qwer", "zxcv", "uiop", "jkl;", "bnm,", "qwer"],
            ),
        ]

        for v, result in results:
            self.assertEqual(list(flatten(v)), result)  # type: ignore
