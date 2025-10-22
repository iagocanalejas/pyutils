import re

CAMEL_TO_SNAKE = re.compile(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z])|(?<=[a-zA-Z])[0-9])")


def camel_to_snake(camel_str: str) -> str:
    """
    Transforms a camelcase string into a snakecase one.
    """
    snake_str = CAMEL_TO_SNAKE.sub(r"_\1", camel_str)
    return snake_str.lower()


def int_to_european(number: int, grouping: bool = False) -> str:
    """
    Formats a number to European format.

    Parameters:
        number (int): the number to transform
        grouping (bool): if format should group the result

    Example:
        int_to_european(1000)
        # 1000,00
        int_to_european(1000, grouping=True)
        # 1.000,00
    """
    integer_part, decimal_part = f"{number:.2f}".split(".")
    if grouping:
        integer_part = ".".join([integer_part[max(i - 3, 0) : i] for i in range(len(integer_part), 0, -3)][::-1])
    return f"{integer_part},{decimal_part}"
