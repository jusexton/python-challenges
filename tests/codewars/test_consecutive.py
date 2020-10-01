from typing import List

import pytest

from challenges.codewars import consecutive


@pytest.mark.parametrize("numbers,count", [
    ([], 0),
    ([1, 2, 3, 4], 2),
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 5, 8, -4, -3, 7, 6, 5], 3),
    ([21, 20, 22, 40, 39, -56, 30, -55, 95, 94], 2),
    ([81, 44, 80, 26, 12, 27, -34, 37, -35], 0)
])
def test_pairs_correctly_counts_consecutive_pairs(numbers: List[int], count: int):
    assert count == consecutive.pairs(numbers)
