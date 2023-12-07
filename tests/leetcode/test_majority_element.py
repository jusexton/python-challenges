import pytest

from challenges.leetcode.majority_element import majority_element


@pytest.mark.parametrize('numbers,expected', [
    ([3, 2, 3], [3]),
    ([1], [1]),
    ([1, 2], [1, 2])
])
def test_majority_element(numbers: list[int], expected: list[int]):
    actual = majority_element(numbers)
    assert actual == expected
