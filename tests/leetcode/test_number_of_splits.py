import pytest

from challenges.leetcode.number_of_splits import ways_to_split_array


@pytest.mark.parametrize(
    "expected, numbers", [(2, [10, 4, -8, 7]), (2, [2, 3, 1, 0]), (0, [-2, -1])]
)
def test_correct_number_of_splits_is_identified(expected: int, numbers: list[int]):
    assert expected == ways_to_split_array(numbers)
