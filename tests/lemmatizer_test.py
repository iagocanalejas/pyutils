from pyutils.strings.lemma import expand_lemmas

expansions: list[list[str | None]] = [
    ["trofeo", "bandera"],
    ["trainera", None],
]


def test_lemma_expansion() -> None:
    assert expand_lemmas(["trofeo", "nombre"], expansions) == [["nombre", "trofeo"], ["nombre", "bandera"]]
