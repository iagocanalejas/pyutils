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
    Convert an integer to a Roman numeral.

    :param num: Integer to convert (must be between 1 and 3999)
    :return: Roman numeral representation of the integer
    """
    val_syms = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    roman_num = []
    for value, symbol in val_syms:
        count, num = divmod(num, value)
        roman_num.append(symbol * count)

    return "".join(roman_num)


def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral to an integer.

    :param s: Roman numeral string (valid input assumed)
    :return: Integer representation of the Roman numeral
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
