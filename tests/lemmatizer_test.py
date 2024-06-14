import unittest

from pyutils.strings.lemma import expand_lemmas


class TestLemmatizer(unittest.TestCase):
    expansions: list[list[str | None]] = []

    def setUp(self):
        self.expansions = [
            ["trofeo", "bandera"],
            ["trainera", None],
        ]

    def test_lemma_expansion(self):
        self.assertEqual(
            expand_lemmas(["trofeo", "nombre"], self.expansions),
            [["nombre", "trofeo"], ["nombre", "bandera"]],
        )
