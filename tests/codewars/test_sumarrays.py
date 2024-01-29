from typing import List

import pytest

from challenges.codewars import sumarrays


@pytest.mark.parametrize(
    "expected,array_one,array_two",
    [
        ([], [], []),
        ([0], [0], []),
        ([1, 5, 6], [1, 5, 6], []),
        ([0], [0], [0]),
        ([1], [0], [1]),
        ([1], [1], [0]),
        ([1, 0], [9], [1]),
        ([0], [-5], [5]),
        ([-1], [-7], [6]),
    ],
)
def test_sum_arrays_correctly_sums_two_given_arrays(
    expected: int, array_one: List[int], array_two: List[int]
):
    assert expected == sumarrays.sum_arrays(array_one, array_two)
