from collections import defaultdict


def is_good(numbers: list[int]) -> bool:
    n = max(numbers)
    expected = {i: 1 for i in range(1, n + 1)}
    expected[n] = 2

    occurrences = defaultdict(int)
    for number in numbers:
        occurrences[number] += 1

    return occurrences == expected
