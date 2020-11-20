from typing import List

import pytest

from challenges.codewars import sortnumbers


@pytest.mark.parametrize('expected,numbers', [
    ([], None),
    ([3, 4, 6], [4, 6, 3]),
    ([1, 2, 5, 10], [1, 2, 10, 5])
])
def test_should_return_given_numbers_in_sorted_list(expected: List[int], numbers: List[int]):
    assert sortnumbers.sort_numbers(numbers) == expected
