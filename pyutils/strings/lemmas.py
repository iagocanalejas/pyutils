def expand_lemmas(lemmas: list[str], expansions: list[list[str | None]]) -> list[list[str]]:
    """
    Expand the original lemmas with optional expansion words to create new combinations.

    The `expand_lemmas` function takes two parameters:
    - lemmas: A list of strings representing the original lemmas (words).
    - expansions: A list of lists, where each inner list contains optional expansion words that can be added
                  to the original lemmas to create new combinations.

    The function generates all possible combinations of lemmas with words from the expansion groups while ensuring
    no duplicates are present in the final result.

    Parameters:
        lemmas (List[str]): A list of strings representing the original lemmas.
        expansions (List[List[Optional[str]]]): A list of lists, where each inner list contains optional expansion
                                                words that can be added to the original lemmas.

    Returns:
        List[List[str]]: A list of lists of strings representing the expanded combinations of the original lemmas
                         with words from the expansion groups.

    Example:
        lemmas = ["cat", "dog"]
        expansions = [["big", "small"], ["red", "blue"]]
        result = expand_lemmas(lemmas, expansions)
        # Output: [['cat', 'big'], ['cat', 'small'], ['dog', 'big'], ['dog', 'small'],
        #          ['cat', 'red'], ['cat', 'blue'], ['dog', 'red'], ['dog', 'blue']]
    """

    expanded_combinations = [lemmas]
    for group in expansions:
        if not any(w in lemmas for w in group):
            continue

        # remove all words from the expanded_combination that will be re-added in the current group
        expanded_combinations = [[w for w in combination if w not in group] for combination in expanded_combinations]

        # add new expansions
        new_expanded_combinations: list[list[str]] = []
        for combination in expanded_combinations:
            for word in group:
                new_combination = combination.copy()
                if word:  # this allows to remove a lemma in a new set
                    new_combination.append(word)
                new_expanded_combinations.append(new_combination)
        expanded_combinations = new_expanded_combinations
    return expanded_combinations


def normalize_synonyms(phrase: str, synonyms: dict[str, list[str]]) -> str:
    """
    Normalize synonyms in a given phrase by replacing them with their corresponding keys.

    The `normalize_synonyms` function takes a phrase and a dictionary of synonyms as input and returns the normalized
    phrase with all the synonyms replaced by their corresponding keys.

    Parameters:
        phrase (str): The input phrase in which synonyms need to be normalized.
        synonyms (Dict[str, List[str]]): A dict containing synonyms as keys and lists of corresponding words as values.

    Returns:
        str: The normalized phrase with all the synonyms replaced by their corresponding keys.

    Example:
        phrase = "a b c d"
        synonyms = {
            "x": ["a", "b"],
            "y": ["c"],
            "z": ["d"]
        }
        result = normalize_synonyms(phrase, synonyms)
        # Output: "x x y z"

        phrase = "I have a good car"
        synonyms = {
            "awesome": ["good", "great"],
            "vehicle": ["car"]
        }
        result = normalize_synonyms(phrase, synonyms)
        # Output: "I have a awesome vehicle"
    """
    for key, options in synonyms.items():
        for option in options:
            phrase = (
                phrase.replace(option, key)
                if " " in option
                else " ".join([part if part != option else key for part in phrase.split()])
            )
    return phrase
