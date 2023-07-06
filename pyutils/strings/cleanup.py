import re
import unicodedata

from .roman import find_roman


def unaccent(text: str) -> str:
    """
    Removes diacritical marks (accents) from characters in the given text.

    :param text: The input string with potential accented characters.
    :return: The modified text without accents.
    """
    return "".join(c for c in unicodedata.normalize("NFD", text) if not unicodedata.combining(c))


def whitespaces_clean(text: str) -> str:
    """
    Removes leading, trailing, and multiple consecutive whitespaces, replacing them with a single space.

    :param text: The input string.
    :return: The cleaned string with normalized whitespace.
    """
    return re.sub(r"\s+", " ", text).strip()


def remove_parenthesis(text: str, preserve_content: bool = False) -> str:
    """
    Removes parentheses and their content from the given text.

    :param text: The input string.
    :param preserve_content: If True, removes only the parentheses but keeps the content inside.
    :return: The modified text without parentheses or their content.
    """
    if preserve_content:
        return whitespaces_clean(text.replace("(", "").replace(")", ""))

    while "(" in text and ")" in text:
        text = re.sub(r"\([^()]*\)", "", text)
    return whitespaces_clean(text)


def remove_brackets(text: str, preserve_content: bool = False) -> str:
    """
    Removes brackets `{}` and `[]` along with their content from the given text.

    :param text: The input string.
    :param preserve_content: If True, removes only the brackets but keeps the content inside.
    :return: The modified text without brackets or their content.
    """
    if preserve_content:
        return whitespaces_clean(text.replace("{", "").replace("}", "").replace("[", "").replace("]", ""))

    while "{" in text and "}" in text:
        text = re.sub(r"\{[^{}]*\}", "", text)
    while "[" in text and "]" in text:
        text = re.sub(r"\[[^\[\]]*\]", "", text)
    return whitespaces_clean(text)


def remove_symbols(text: str, preserve_quotes: bool = False) -> str:
    """
    Removes symbols from the given text while optionally preserving quotes.

    :param text: The input string.
    :param preserve_quotes: If True, keeps single and double quotes.
    :return: The cleaned text without unwanted symbols.
    """
    allowed_pattern = r"[^\w\s\-\"']" if preserve_quotes else r"[^\w\s\-]"
    text = re.sub(allowed_pattern, "", text)
    return whitespaces_clean(text)


def remove_hyphens(word: str) -> str:
    """
    Removes leading and trailing hyphens from a word.

    :param word: The input string.
    :return: The modified string without leading or trailing hyphens.
    """
    return remove_leading_hyphen(remove_trailing_hyphen(word))


def remove_leading_hyphen(word: str) -> str:
    """
    Removes a leading hyphen (optionally followed by a space) from a word.

    :param word: The input string.
    :return: The modified string without a leading hyphen.
    """
    return re.sub(r"^\s*-+\s*", "", word).strip()


def remove_trailing_hyphen(word: str) -> str:
    """
    Removes a trailing hyphen (optionally followed by a space) from a word.

    :param word: The input string.
    :return: The modified string without a trailing hyphen.
    """
    return re.sub(r"\s*-+\s*$", "", word).strip()


def remove_roman(text: str) -> str:
    """
    Removes Roman numerals from a given text.

    :param text: The input string.
    :return: The text without Roman numerals.
    """
    return whitespaces_clean(" ".join(w for w in text.split() if find_roman(re.sub(r"[\'\".:]", "", w)) is None))


GENDERS = [
    "FEMENINA",
    "FEMENINO",
    "MASCULINA",
    "MASCULINO",
    "FEMININA",
    "FEMININO",
    "FEMINAS",
    "EMAKUMEEN",
    "EMAKUMEAK",
    "NESKEN",
    "NESKA",
    "EMAKUMEZKOEN",
]


def remove_genders(text: str) -> str:
    """
    :return text without gendered words
    """
    return " ".join(i for i in text.split() if i not in GENDERS)


CONJUNCTIONS = [
    "EL",
    "LA",
    "LOS",
    "LAS",
    "O",
    "A",
    "OS",
    "AS",
    "DE",
    "DA",
    "DO",
    "DAS",
    "DOS",
    "DEL",
    "L",
    "ELS",
    "LES",
    "SES",
    "ES",
    "SA",
    "POR",
    "Y",
]


def remove_conjunctions(text: str) -> str:
    """
    :return: text without conjunctions
    """
    return " ".join(i for i in text.split() if i not in CONJUNCTIONS)


def lstrip_conjunctions(text: str) -> str:
    """
    :return: text without starter conjunctions
    """
    words = text.split()
    for idx, word in enumerate(words):
        if word not in CONJUNCTIONS:
            return " ".join(words[idx:])
    return ""
