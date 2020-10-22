from typing import List


def parts_sums(arr: List[int]) -> List[int]:
    parts = [sum(arr)]
    for index in range(len(arr)):
        new = parts[index] - arr[index]
        parts.append(new)

    return parts

