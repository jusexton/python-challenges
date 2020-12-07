# First attempt. Did not work for all cases
# def minimum_steps(string_one: str, string_two: str) -> int:
#     sorted_one = sorted(string_one)
#     sorted_two = sorted(string_two)
#
#     if sorted_one == sorted_two:
#         return 0
#
#     return sum(0 if a == b else 1 for a, b in zip(sorted_one, sorted_two))

from collections import Counter


def minimum_steps(string_one: str, string_two: str) -> int:
    one_count = Counter(string_one)
    two_count = Counter(string_two)

    steps = 0
    for char, count in one_count.items():
        two_char_count = two_count.get(char) or 0
        needed = count - two_char_count
        steps += 0 if needed < 0 else needed

    return steps
