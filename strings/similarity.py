from difflib import SequenceMatcher
from typing import List, Optional, Tuple


def levenshtein_distance(s1: str, s2: str) -> float:
    # Create a matrix with dimensions (len(s1) + 1) x (len(s2) + 1)
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize the first row and column of the matrix
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j

    # Compute the Levenshtein distance
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,  # Deletion
                matrix[i][j - 1] + 1,  # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    # The Levenshtein distance is the value in the bottom-right cell of the matrix
    return matrix[-1][-1]


def closest_result(keyword: str, elements: List[str]) -> Tuple[Optional[str], float]:
    if any(e == keyword for e in elements):
        return keyword, 1.

    best_distance = SequenceMatcher(a=keyword, b=elements[0]).ratio()
    best_word = elements[0]
    for possibility in elements:
        if all(w in keyword for w in possibility.split()) and all(w in possibility for w in keyword.split()):
            return possibility, 1.

        d = SequenceMatcher(a=keyword, b=possibility).ratio()
        if d > best_distance:
            best_distance = d
            best_word = possibility

    return best_word, best_distance
