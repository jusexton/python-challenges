from collections import Counter
from typing import List


# There is a bug with this solution
# The values 2,3,6,7 xor to 0
# def can_equal(target: List[int], arr: List[int]) -> bool:
#     return functools.reduce((lambda x, y: x ^ y), target + arr, 0) == 0

def can_equal(target: List[int], arr: List[int]) -> bool:
    return Counter(target) == Counter(arr)
