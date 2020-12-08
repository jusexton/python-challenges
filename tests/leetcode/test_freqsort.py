from typing import List

import pytest

from challenges.leetcode import freqsort


@pytest.mark.parametrize('expected,numbers', [
    ([], []),
    ([2, 2, 1, 1, 1, 1], [1, 2, 2, 1, 1, 1]),
    ([1, 3, 3, 2, 2], [2, 3, 1, 3, 2]),
    ([1, 3, 3, 2, 2], [2, 2, 1, 3, 3])
])
def test_numbers_are_returned_sorted_by_frequency(expected: List[int], numbers: List[int]):
    assert freqsort.frequency_sort(numbers) == expected
