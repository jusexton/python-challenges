def vowel_strings(words: list[str], queries: list[list[int]]) -> list[int]:
    vowels = {"a", "e", "i", "o", "u"}
    ps = [0]
    for word in words:
        vowel_str = word[0] in vowels and word[-1] in vowels
        ps.append(ps[-1] + vowel_str)

    return [ps[right + 1] - ps[left] for [left, right] in queries]
