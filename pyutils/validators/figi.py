def is_valid_figi(figi: str) -> bool:
    if len(figi) != 12:
        return False

    # Converts a character to its numeric value
    def char_to_value(c):
        if c.isdigit():
            return int(c)
        else:
            return ord(c.upper()) - ord("A") + 10

    total = 0
    for i, char in enumerate(figi[:-1]):  # Ignore the last character (checksum digit)
        value = char_to_value(char)
        total += value
        total *= 2 if i % 2 == 0 else 1  # Double it on even positions (starting from index 0)

    checksum = (10 - (total % 10)) % 10
    return str(checksum) == figi[-1]
