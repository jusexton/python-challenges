from typing import List


def diagonal_sum(matrix: List[List[int]]) -> int:
    size = len(matrix)
    summation = 0
    for index in range(0, size):
        summation += matrix[index][index]
        summation += matrix[size - index - 1][index]

    even_length = size % 2 == 0
    return summation if even_length else summation - matrix[size // 2][size // 2]
