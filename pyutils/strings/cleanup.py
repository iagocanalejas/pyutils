import re

from .roman import find_roman


def whitespaces_clean(word: str) -> str:
    return re.sub(r"\s", " ", re.sub(r"\s+", " ", word)).strip()


def remove_parenthesis(word: str) -> str:
    return whitespaces_clean(re.sub(r"\([\w\-_−–#: !+]*\)", "", word))


def remove_symbols(word: str, preserve_quotes: bool = False) -> str:
    word = re.sub(r"[^\S\- ]", "", word)
    if not preserve_quotes:
        # maybe I'm dumb but I'm unable to do this within the regex
        word = word.replace('"', " ").replace("'", " ")
    return whitespaces_clean(word)


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
