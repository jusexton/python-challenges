def prefix_count(self, words: list[str], pref: str) -> int:
    return sum(1 for word in words if word.startswith(pref))
