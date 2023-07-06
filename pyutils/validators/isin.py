import re


def is_valid_isin(isin: str) -> bool:
    # Check the format: 2 letters followed by 10 alphanumeric characters
    if not re.match(r"^[A-Z]{2}[A-Z0-9]{9}[0-9]$", isin):
        return False

    # Convert letters to numbers (A=10, B=11, ..., Z=35)
    def char_to_number(ch):
        if ch.isdigit():
            return ch
        return str(ord(ch.upper()) - 55)  # A=65 -> 10

    # Convert ISIN to a string of digits
    digits = "".join(char_to_number(ch) for ch in isin)

    # Apply Luhn algorithm
    def luhn_checksum(number: str) -> bool:
        total = 0
        reverse_digits = number[::-1]
        for i, d in enumerate(reverse_digits):
            n = int(d)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    return luhn_checksum(digits)
