import pytest

from challenges.leetcode.minimum_operations import min_operations


@pytest.mark.parametrize("n,expected", [(2, 1), (3, 2), (6, 9)])
def test_min_operations(n: int, expected: int):
    actual = min_operations(n)
    assert actual == expected
