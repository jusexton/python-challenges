import math


def count_ones(left: int, right: int) -> int:
    return count_bits(right) - count_bits(left - 1)


def count_bits(number: int) -> int:
    return sum(column_count(column, number) for column in range(64))


def column_count(column: int, number: int) -> int:
    """
    Returns the number of bits in a specified column of bits produced from a given number

    0  0 0 0 0
    1  0 0 0 1
    2  0 0 1 0
    3  0 0 1 1
    4  0 1 0 0
    5  0 1 0 1
       0 2 2 3 - Column bit sums

    :param column: The column to count
    :param number: The number that will be used to "generate" the column of bits
    :return: The total number of bits in the column
    """
    div = (number + 1) / (2 << column)
    summation = math.floor(div)
    rest = max(0, int((div - summation) * (2 << column) - (1 << column)))
    return summation * (1 << column) + rest
