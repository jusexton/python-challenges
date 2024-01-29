import pytest

from challenges.leetcode import canequal


@pytest.mark.parametrize(
    "expected,target,arr",
    [
        (True, [], []),
        (True, [1, 2], [1, 2]),
        (True, [1, 2], [2, 1]),
        (True, [5, 9, 6], [6, 9, 5]),
        (False, [2, 3], [6, 7]),
        (False, [1, 2, 3], [1, 4, 1]),
        (False, [1, 2, 3], [1, 5]),
        (False, [1, 2, 3], [1, 4, 6]),
    ],
)
def test_correctly_returns_whether_two_arrays_can_be_equal(expected, target, arr):
    assert canequal.can_equal(target, arr) == expected
