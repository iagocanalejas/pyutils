import re


def is_valid_email(email: str) -> bool:
    """
    :return: True if the email is valid
    """
    return bool(re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email))
