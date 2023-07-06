import pytest

from pyutils.strings import (
    remove_brackets,
    remove_hyphens,
    remove_parenthesis,
    remove_roman,
    remove_symbols,
    unaccent,
    whitespaces_clean,
)


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("café", "cafe"),
        ("naïve", "naive"),
        ("élève", "eleve"),
        ("München", "Munchen"),
        ("façade", "facade"),
        ("São Paulo", "Sao Paulo"),
        ("résumé", "resume"),
        ("jalapeño", "jalapeno"),
        ("déjà vu", "deja vu"),
        ("crème brûlée", "creme brulee"),
        ("touché", "touche"),
    ),
)
def test_unaccent(text: str, expected: str) -> None:
    assert unaccent(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("  Hello   world!  ", "Hello world!"),
        ("This\nis\ta\ttest", "This is a test"),
        (" Multiple   spaces ", "Multiple spaces"),
        ("\t Tabs \t and \n newlines ", "Tabs and newlines"),
        ("Hello     world", "Hello world"),
        ("   ", ""),  # Edge case: Only spaces should be removed
        ("\n\t   ", ""),  # Edge case: Only tabs/newlines should be removed
        (" A  B  C ", "A B C"),
        ("NoExtraSpacesHere", "NoExtraSpacesHere"),  # No change expected
        ("Mix of spaces\tand newlines\nhere", "Mix of spaces and newlines here"),
    ],
)
def test_whitespaces_clean(text: str, expected: str) -> None:
    assert whitespaces_clean(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello (world)", "Hello"),
        ("Keep (this) and remove (that)", "Keep and remove"),
        ("Nested (example (inner) text)", "Nested"),
        ("No parentheses here", "No parentheses here"),
        ("(Only parentheses)", ""),
        ("Text before (remove this) text after", "Text before text after"),
        ("Multiple (one) (two) (three)", "Multiple"),
    ],
)
def test_remove_parenthesis(text: str, expected: str) -> None:
    assert remove_parenthesis(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello (world)", "Hello world"),
        ("Keep (this) and remove (that)", "Keep this and remove that"),
        ("Nested (example (inner) text)", "Nested example inner text"),
        ("(Only parentheses)", "Only parentheses"),
        ("Multiple (one) (two) (three)", "Multiple one two three"),
    ],
)
def test_remove_parenthesis_preserve_content(text: str, expected: str) -> None:
    assert remove_parenthesis(text, preserve_content=True) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello {world}", "Hello"),
        ("Keep {this} and remove {that}", "Keep and remove"),
        ("Nested {example {inner} text}", "Nested"),
        ("No brackets here", "No brackets here"),
        ("{Only brackets}", ""),
        ("Text before {remove this} text after", "Text before text after"),
        ("Multiple {one} {two} {three}", "Multiple"),
        ("Brackets [example] removed", "Brackets removed"),
        ("Nested [text [inside] here]", "Nested"),
        ("Mixed {curly} and [square] brackets", "Mixed and brackets"),
        ("Multiple [one] [two] [three]", "Multiple"),
    ],
)
def test_remove_brackets(text: str, expected: str) -> None:
    assert remove_brackets(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello {world}", "Hello world"),
        ("Keep {this} and remove {that}", "Keep this and remove that"),
        ("Nested {example {inner} text}", "Nested example inner text"),
        ("{Only brackets}", "Only brackets"),
        ("Multiple {one} {two} {three}", "Multiple one two three"),
        ("Brackets [example] removed", "Brackets example removed"),
        ("Nested [text [inside] here]", "Nested text inside here"),
        ("Mixed {curly} and [square] brackets", "Mixed curly and square brackets"),
        ("Multiple [one] [two] [three]", "Multiple one two three"),
    ],
)
def test_remove_brackets_preserve_content(text: str, expected: str) -> None:
    assert remove_brackets(text, preserve_content=True) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello, World!", "Hello World"),
        ("Python@3.9", "Python39"),
        ("Test123#", "Test123"),
        ("well-known", "well-known"),
        ("hyphen-ated-word!", "hyphen-ated-word"),
        ("\"Hello\" and 'World'", "Hello and World"),
        ("It's a test.", "Its a test"),
        ("   Hello   World!!  ", "Hello World"),
        ("Multiple    spaces...here", "Multiple spaceshere"),
        ("123 abc!@#", "123 abc"),
        ("Keep 100%!", "Keep 100"),
    ],
)
def test_remove_symbols(text: str, expected: str) -> None:
    assert remove_symbols(text) == expected


def test_remove_symbols_preserve_quotes() -> None:
    # fmt: off
    assert remove_symbols("\"Hello\" and 'World'", preserve_quotes=True) == "\"Hello\" and \'World\'"
    assert remove_symbols("He said: 'Yes!'", preserve_quotes=True) == "He said \'Yes\'"
    assert remove_symbols('"Python" is fun!', preserve_quotes=True) == '"Python" is fun'
    # fmt: on


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello IX world", "Hello world"),
        ("CD is 400, XL is 40", "is 400, is 40"),
        ("This is the year MMXXV", "This is the year"),
        ("123 and XX should not be removed", "123 and should not be removed"),
        ("ROMAN NUMERALS: I II III IV V VI VII VIII IX X", "ROMAN NUMERALS:"),
        ("MCMXCIV is 1994, but not in 2024", "is 1994, but not in 2024"),
        ("Invalid numerals ABCD XYZ stay", "Invalid numerals ABCD XYZ stay"),
        ("Quotes 'XIV' should also be removed.", "Quotes should also be removed."),
    ],
)
def test_remove_roman(text: str, expected: str) -> None:
    assert remove_roman(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello-world", "Hello-world"),
        ("--Leading", "Leading"),
        ("Trailing--", "Trailing"),
        ("--Both--", "Both"),
        ("--Multiple--hyphens--", "Multiple--hyphens"),
        ("--  --", ""),
        ("---", ""),
        ("No hyphens here", "No hyphens here"),
        ("--Multiple--hyphens--inside--", "Multiple--hyphens--inside"),
    ],
)
def test_remove_hyphens(text: str, expected: str) -> None:
    assert remove_hyphens(text) == expected
