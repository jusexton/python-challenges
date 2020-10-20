from typing import List


def cut_the_ropes(values: List[int]):
    values = sorted(values)
    result = []

    while len(values) > 0:
        first = values[0]
        result.append(len(values))
        values = [value - first for value in values if value - first != 0]

    return result
