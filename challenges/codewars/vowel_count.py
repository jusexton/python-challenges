def vowel_count(s: str) -> int:
    return sum(c in 'aeiou' for c in s)
