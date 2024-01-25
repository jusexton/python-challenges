import pytest

from challenges.leetcode import counting_bits


@pytest.mark.parametrize(
    "expected,n",
    [([0, 1, 1, 2, 1, 2], 5), ([0, 1, 1], 2), ([0, 1, 1, 2, 1, 2, 2, 3], 7)],
)
def test_should_return_correct_day_of_week(expected: list[int], n: int):
    actual = counting_bits.count_bits(n)
    assert actual == expected
