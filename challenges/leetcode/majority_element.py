from collections import Counter


def majority_element(numbers: list[int]) -> list[int]:
    req_freq = len(numbers) // 3
    num_freq = Counter(numbers)
    return [k for k, v in num_freq.items() if v > req_freq]
