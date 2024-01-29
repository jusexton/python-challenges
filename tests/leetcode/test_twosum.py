import pytest

from challenges.leetcode import twosum


@pytest.mark.parametrize(
    "expected,numbers,target",
    [
        ([0, 1], [2, 7, 9, 10], 9),
        ([1, 2], [2, 7, 9, 10], 16),
        ([0, 3], [2, 7, 9, 10], 12),
        ([2, 3], [2, 7, 9, 10], 19),
    ],
)
def test_should_return_correct_indices(expected, numbers, target):
    assert expected == twosum.two_sum(numbers, target)


@pytest.mark.parametrize("numbers,target", [([0], -1), ([0, 1], 9)])
def test_should_raise_value_error_when_result_does_not_exist(numbers, target):
    with pytest.raises(ValueError):
        twosum.two_sum(numbers, target)
