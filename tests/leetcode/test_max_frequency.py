import pytest

from challenges.leetcode.max_frequency import max_frequency_elements


@pytest.mark.parametrize("expected,numbers", [(3, [1, 2, 3]), (4, [1, 1, 2, 2, 3])])
def test_max_frequency_elements(expected: int, numbers: list[int]):
    actual = max_frequency_elements(numbers)
    assert actual == expected
