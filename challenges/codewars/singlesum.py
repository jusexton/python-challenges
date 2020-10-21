from collections import Counter
from typing import List


def single_sum(numbers: List[int]) -> int:
    return sum(number for number, count in Counter(numbers).items() if count == 1)
