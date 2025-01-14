from collections import Counter


def unique_occurrences(arr: list[int]) -> bool:
    counts = Counter(arr)
    return len(set(counts.values())) == len(counts)
