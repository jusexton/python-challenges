import math
from typing import List


def least_larger(values: List[int], index: int) -> int:
    target = values[index]
    possible = (math.inf, None)
    for index, value in enumerate(values):
        if target < value < possible[0]:
            possible = (value, index)

    return -1 if possible[0] == math.inf else possible[1] # type: ignore
