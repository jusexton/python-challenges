from typing import List

import pytest

from challenges.codewars import singlesum


@pytest.mark.parametrize('expected,numbers', [
    (0, []),
    (1, [1]),
    (1, [1, 2, 2]),
    (0, [1, 1, 2, 2]),
    (3, [1, 1, 2, 2, 3]),
])
def test_should_return_the_sum_of_non_repeating_values(expected: int, numbers: List[int]):
    assert expected == singlesum.single_sum(numbers)
