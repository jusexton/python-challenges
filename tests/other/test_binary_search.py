import pytest

from challenges.other import binary_search


@pytest.mark.parametrize(
    "sorted_array,value,expected",
    [
        ([], 5, -1),
        ([1], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1),
        ([1, 2, 3, 4, 5, 6], 3, 2),
        ([1, 2, 3, 4, 5, 6], 4, 3),
    ],
)
def test_binary_search(sorted_array: list[int], value: int, expected: int):
    assert binary_search.search(sorted_array, value) == expected
