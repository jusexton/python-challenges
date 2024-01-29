from collections import Counter


def max_frequency_elements(numbers: list[int]) -> int:
    freq = Counter(numbers)
    max_freq = max(freq.values())
    return sum(value for value in freq.values() if value == max_freq)
