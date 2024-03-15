import re
import unicodedata

from .roman import find_roman


def unaccent(text: str) -> str:
    """
    :return text without accents
    """
    return "".join(c for c in unicodedata.normalize("NFD", text) if not unicodedata.combining(c))


def whitespaces_clean(text: str) -> str:
    """
    :return text without leading, trailing and multiple whitespaces
    """
    return re.sub(r"\s", " ", re.sub(r"\s+", " ", text)).strip()


def remove_parenthesis(text: str) -> str:
    """
    :return text without parenthesis and its content
    """
    return whitespaces_clean(re.sub(r"\([\w\-_−–#: !+]*\)", "", text))


def remove_symbols(text: str, preserve_quotes: bool = False) -> str:
    """
    :return text without symbols
    """
    text = re.sub(r"[^\S\- ]", "", text)
    if not preserve_quotes:
        # maybe I'm dumb but I'm unable to do this within the regex
        text = text.replace('"', " ").replace("'", " ")
    return whitespaces_clean(text)


def remove_roman(text: str) -> str:
    """
    :return text without roman numbers
    """
    return whitespaces_clean(" ".join(w for w in text.split() if find_roman(re.sub(r"[\'\".:]", "", w)) is None))


def remove_genders(text: str) -> str:
    """
    :return text without gendered words
    """
    genders = [
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
    return " ".join(i for i in text.split() if i not in genders)


def remove_conjunctions(text: str) -> str:
    """
    :return: text without conjunctions
    """
    conjunctions = [
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
        "Y",
    ]
    return " ".join(i for i in text.split() if i not in conjunctions)
