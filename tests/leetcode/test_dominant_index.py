import pytest

from challenges.leetcode.dominant_index import dominant_index


@pytest.mark.parametrize(
    "expected,numbers", [(1, [5, 10, 1, 5, 2]), (-1, [1, 2, 3, 4])]
)
def test_dominant_index_is_returned(expected: int, numbers: list[int]):
    actual = dominant_index(numbers)
    assert expected == actual
