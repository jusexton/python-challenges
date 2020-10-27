from typing import List


def pyramid(n: int) -> List[List[int]]:
    return [[1] * i for i in range(1, n + 1)]
