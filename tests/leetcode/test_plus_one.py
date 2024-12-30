import pytest

from challenges.leetcode import plus_one


@pytest.mark.parametrize("expected,digits", [([1, 0], [9]), ([1, 3], [1, 2])])
def test_adds_one_to_digits(expected: list[int], digits: list[int]):
    assert expected == plus_one.plus_one(digits)
