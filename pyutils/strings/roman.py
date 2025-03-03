import re


def find_roman(word: str) -> str | None:
    """
    Checks if a word is a valid Roman numeral.

    :param word: The input string.
    :return: The word itself if it's a valid Roman numeral, otherwise None.
    """
    roman_pattern = r"^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$"
    return word if re.match(roman_pattern, word) else None


def int_to_roman(num: int) -> str:
    """
    :return: converts an integer number to a roman number
    """
    val = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    roman_num = ""
    for i in range(len(val)):
        count = int(num / val[i])
        roman_num += syb[i] * count
        num -= val[i] * count
    return roman_num


def roman_to_int(s: str) -> int:
    """
    :return: converts a roman number to an integer number
    """
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i : i + 2] in roman:
            num += roman[s[i : i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num
