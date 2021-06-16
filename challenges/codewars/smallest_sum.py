from functools import reduce
from math import gcd
from typing import List


def smallest_sum(values: List[int]):
    return reduce(gcd, values) * len(values)
