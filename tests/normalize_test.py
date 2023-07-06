import pytest

from pyutils.strings.normalize import apply_replaces

normalizations = {
    "brown": ["brwn", "brn"],
    "fox": ["fx"],
    "over": ["ovr"],
    "dog": ["dg"],
}


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("The quick brwn fx jumps ovr the lazy dg", "The quick brown fox jumps over the lazy dog"),
    ],
)
def test_apply_replaces(text: str, expected: str) -> None:
    assert apply_replaces(text, normalizations) == expected
