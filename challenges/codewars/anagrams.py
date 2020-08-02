def is_anagram(test: str, original: str) -> bool:
    if len(test) != len(original):
        return False

    balance = 0
    for character in (test + original).lower():
        balance ^= ord(character)

    return balance == 0
