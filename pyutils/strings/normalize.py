def match_normalization(text: str, normalization_rules: dict[str, list[list[str]]]) -> str:
    """
    Applies normalization rules to the input text based on provided patterns.

    Parameters:
        text (str): The input text to be normalized.
        normalization_rules (dict[str, list[list[str]]]): A dictionary containing normalization rules.
            Each key represents a normalized value, and its corresponding value is a list of lists of strings.
            Each inner list represents a pattern. The function will return the normalized value of the first
            pattern that matches the input text.

    Returns:
        str: The normalized text, or the original text if no normalization rule is applied.

    Examples:
        >>> normalization_rules = {
        ...     "number": [["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]],
        ...     "place": [["Paris", "London", "New York", "Tokyo"]]
        ... }
        >>> apply_normalization_rules("I will be in Paris next Monday", normalization_rules)
        'place'
        >>> apply_normalization_rules("I will be in London next Monday", normalization_rules)
        'place'
        >>> apply_normalization_rules("I have two apples", normalization_rules)
        'number'
        >>> apply_normalization_rules("No normalization needed", normalization_rules)
        'No normalization needed'
    """
    for normalized_value, patterns in normalization_rules.items():
        for pattern in patterns:
            if all(v in text.split() for v in pattern):
                return normalized_value
    return text


def apply_replaces(text: str, normalizations: dict[str, list[str]]) -> str:
    """
    Apply a set of normalizations to a given text.

    This function replaces specific substrings within the input text
    with their corresponding normalization keys, based on the provided
    dictionary of normalizations.

    Parameters:
        text (str): The input text to be normalized.
        normalizations (dict[str, list[str]]): A dictionary where keys
            represent normalization keys and values are lists of substrings
            to be replaced by the corresponding key.

    Returns:
        str: The normalized text.

    Examples:
        >>> text = "The quick brwn fx jumps ovr the lazy dg."
        >>> normalizations = {
        ...     "brown": ["brwn", "brn"],
        ...     "fox": ["fx"],
        ...     "over": ["ovr"],
        ...     "dog": ["dg"]
        ... }
        >>> apply_normalizations(text, normalizations)
        'The quick brown fox jumps over the lazy dog.'

        >>> text = "I luv Python, it's the best!"
        >>> normalizations = {
        ...     "love": ["luv", "like"],
        ...     "Python": ["Python", "programming language"]
        ... }
        >>> apply_normalizations(text, normalizations)
        "I love Python, it's the best!"
    """
    for k, values in normalizations.items():
        if any(v in text.split() for v in values) and k not in text:
            for v in values:
                text = text.replace(v, k)
            return text
    return text
