def max_vowels(s: str, k: int) -> int:
    curr_count = max_count = sum(1 for char in s[:k] if char in "aeiouAEIOU")
    for i in range(k, len(s)):
        curr_count += s[k] in "aeiouAEIOU"
        curr_count -= s[i - k] in "aeiouAEIOU"
        max_count = max(max_count, curr_count)
    return max_count
