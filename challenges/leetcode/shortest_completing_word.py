from collections import Counter


def shortest_completing_word(license_plate: str, words: list[str]) -> str:
    plate_chars = Counter(c for c in license_plate.lower() if c.isalpha())
    matches = [word for word in words if Counter(word) >= plate_chars]
    return min(matches, key=len)
