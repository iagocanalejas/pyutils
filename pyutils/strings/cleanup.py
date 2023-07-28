import re
from .roman import find_roman


def whitespaces_clean(word: str) -> str:
    return re.sub(r"\s", " ", re.sub(r"\s+", " ", word)).strip()


def remove_parenthesis(word: str) -> str:
    return whitespaces_clean(re.sub(r"\([\w\-_−–#: !+]*\)", "", word))


def remove_symbols(word: str, ignore_quotes: bool = False) -> str:
    reg = r'[^\S\-"\'<>]' if ignore_quotes else r"[^\S\-<>]"
    return whitespaces_clean(re.sub(reg, " ", word))


def remove_roman(word: str) -> str:
    return whitespaces_clean(" ".join(w for w in word.split() if find_roman(re.sub(r"[\'\".:]", "", w)) is None))


def remove_conjunctions(word: str) -> str:
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
    return " ".join(i for i in word.split() if i not in conjunctions)