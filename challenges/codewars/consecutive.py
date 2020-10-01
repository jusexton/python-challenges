from typing import List


def pairs(numbers: List[int]) -> int:
    return sum(_consecutive(a, b) for a, b in zip(numbers[::2], numbers[1::2]))


def _consecutive(number_one: int, number_two: int) -> bool:
    return abs(number_one - number_two) == 1

# def pairs(numbers: List[int]) -> int:
#     consecutive_count = 0
#     for index in range(0, len(numbers) - 1, 2):
#         if _consecutive(numbers[index], numbers[index + 1]):
#             consecutive_count += 1
#
#     return consecutive_count
#
#
