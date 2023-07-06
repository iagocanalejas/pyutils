import unittest

from pyutils.strings import (
    remove_brackets,
    remove_hyphens,
    remove_parenthesis,
    remove_roman,
    remove_symbols,
    unaccent,
    whitespaces_clean,
)


class TestCleanup(unittest.TestCase):
    def test_unaccent(self) -> None:
        values = [
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
        ]

        for v, r in values:
            self.assertEqual(unaccent(v), r)

    def test_whitespaces_clean(self) -> None:
        values = [
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
        ]

        for v, r in values:
            self.assertEqual(whitespaces_clean(v), r)

    def test_remove_parenthesis(self) -> None:
        values = [
            ("Hello (world)", "Hello"),
            ("Keep (this) and remove (that)", "Keep and remove"),
            ("Nested (example (inner) text)", "Nested"),
            ("No parentheses here", "No parentheses here"),
            ("(Only parentheses)", ""),
            ("Text before (remove this) text after", "Text before text after"),
            ("Multiple (one) (two) (three)", "Multiple"),
        ]
        for v, r in values:
            self.assertEqual(remove_parenthesis(v), r)

    def test_remove_parenthesis_preserve_content(self) -> None:
        values = [
            ("Hello (world)", "Hello world"),
            ("Keep (this) and remove (that)", "Keep this and remove that"),
            ("Nested (example (inner) text)", "Nested example inner text"),
            ("(Only parentheses)", "Only parentheses"),
            ("Multiple (one) (two) (three)", "Multiple one two three"),
        ]
        for v, r in values:
            self.assertEqual(remove_parenthesis(v, preserve_content=True), r)

    def test_remove_brackets(self) -> None:
        values = [
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
        ]
        for v, r in values:
            self.assertEqual(remove_brackets(v), r)

    def test_remove_brackets_preserve_content(self) -> None:
        values = [
            ("Hello {world}", "Hello world"),
            ("Keep {this} and remove {that}", "Keep this and remove that"),
            ("Nested {example {inner} text}", "Nested example inner text"),
            ("{Only brackets}", "Only brackets"),
            ("Multiple {one} {two} {three}", "Multiple one two three"),
            ("Brackets [example] removed", "Brackets example removed"),
            ("Nested [text [inside] here]", "Nested text inside here"),
            ("Mixed {curly} and [square] brackets", "Mixed curly and square brackets"),
            ("Multiple [one] [two] [three]", "Multiple one two three"),
        ]
        for v, r in values:
            self.assertEqual(remove_brackets(v, preserve_content=True), r)

    def test_remove_symbols(self) -> None:
        values = [
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
        ]

        for v, r in values:
            self.assertEqual(remove_symbols(v), r)

    def test_remove_symbols_preserve_quotes(self) -> None:
        # fmt: off
        self.assertEqual(remove_symbols("\"Hello\" and 'World'", preserve_quotes=True), "\"Hello\" and \'World\'")
        self.assertEqual(remove_symbols("He said: 'Yes!'", preserve_quotes=True), "He said \'Yes\'")
        self.assertEqual(remove_symbols('"Python" is fun!', preserve_quotes=True), '"Python" is fun')
        # fmt: on

    def test_remove_roman(self) -> None:
        values = [
            ("Hello IX world", "Hello world"),
            ("CD is 400, XL is 40", "is 400, is 40"),
            ("This is the year MMXXV", "This is the year"),
            ("123 and XX should not be removed", "123 and should not be removed"),
            ("ROMAN NUMERALS: I II III IV V VI VII VIII IX X", "ROMAN NUMERALS:"),
            ("MCMXCIV is 1994, but not in 2024", "is 1994, but not in 2024"),
            ("Invalid numerals ABCD XYZ stay", "Invalid numerals ABCD XYZ stay"),
            ("Quotes 'XIV' should also be removed.", "Quotes should also be removed."),
        ]

        for v, r in values:
            self.assertEqual(remove_roman(v), r)

    def test_remove_hyphens(self) -> None:
        values = [
            ("Hello-world", "Hello-world"),
            ("--Leading", "Leading"),
            ("Trailing--", "Trailing"),
            ("--Both--", "Both"),
            ("--Multiple--hyphens--", "Multiple--hyphens"),
            ("--  --", ""),
            ("---", ""),
            ("No hyphens here", "No hyphens here"),
            ("--Multiple--hyphens--inside--", "Multiple--hyphens--inside"),
        ]

        for v, r in values:
            self.assertEqual(remove_hyphens(v), r)
