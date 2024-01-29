from typing import List

import pytest

from challenges.leetcode import diagonalsum


@pytest.mark.parametrize(
    "expected,matrix",
    [
        (5, [[5]]),
        (10, [[1, 2], [3, 4]]),
        (25, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        (8, [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]),
    ],
)
def test_returns_sum_of_given_matrix_diagonals(expected: int, matrix: List[List[int]]):
    assert diagonalsum.diagonal_sum(matrix) == expected
