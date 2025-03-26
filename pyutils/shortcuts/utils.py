import uuid


def generate_unique_code(length: int = 8) -> str:
    """
    :return: Generated 'length' length hexadecimal number
    """
    return uuid.uuid4().hex[:length].upper()
