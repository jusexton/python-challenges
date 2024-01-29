from typing import List

import pytest

from challenges.codewars import smallest_sum


@pytest.mark.parametrize(
    "expected,values", [(9, [9]), (9, [6, 9, 21]), (3, [1, 21, 55])]
)
def test_should_return_the_smallest_sum(expected: int, values: List[int]):
    assert smallest_sum.smallest_sum(values) == expected
