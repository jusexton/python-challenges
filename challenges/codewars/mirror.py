from typing import List


def mirror(items: List[int]) -> List[int]:
    sorted_items = sorted(items)
    return sorted_items + sorted_items[-2::-1]
