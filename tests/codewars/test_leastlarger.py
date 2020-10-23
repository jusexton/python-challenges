from typing import List

import pytest

from challenges.codewars import least_larger


@pytest.mark.parametrize("expected,values,index", [
    (3, [4, 1, 3, 5, 6], 0),
    (-1, [4, 1, 3, 5, 6], 4)
])
def test_returns_the_least_largest_value_from_given_index_value(
        expected: int, values: List[int], index: int):
    assert least_larger.least_larger(values, index) == expected
