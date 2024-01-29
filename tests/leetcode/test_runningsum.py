from typing import List

import pytest

from challenges.leetcode import runningsum


@pytest.mark.parametrize(
    "expected,numbers", [([0], []), ([1, 3], [1, 2]), ([5, 15, 30], [5, 10, 15])]
)
def test_running_sum_is_correctly_returned(expected: List[int], numbers: List[int]):
    assert runningsum.running_sum(numbers) == expected
