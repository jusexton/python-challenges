import sys


def increasing_triplet(numbers: list[int]) -> bool:
    small, mid = sys.maxsize, sys.maxsize
    for number in numbers:
        if number <= small:
            small = number
        elif number <= mid:
            mid = number
        else:
            return True
    return False
