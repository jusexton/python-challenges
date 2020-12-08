from collections import Counter
from typing import List


def frequency_sort(numbers: List[int]) -> List[int]:
    counter = Counter(numbers)
    return sorted(numbers, key=lambda x: (counter[x], -x))
