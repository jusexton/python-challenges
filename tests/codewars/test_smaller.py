import pytest

from challenges.codewars import smaller


@pytest.mark.parametrize(
    "numbers,expected", [([5, 4, 3, 2, 1], [4, 3, 2, 1, 0]), ([1, 2, 0], [1, 1, 0])]
)
def test_array_with_correct_counts_is_returned(numbers: list[int], expected: int):
    assert expected == smaller.smaller(numbers)
