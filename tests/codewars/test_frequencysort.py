import pytest

from challenges.codewars import frequencysort


@pytest.mark.parametrize(
    "expected,items",
    [
        ([3, 3, 3, 5, 5, 7, 7, 2, 9], [2, 3, 5, 3, 7, 9, 5, 3, 7]),
        (
            [1, 1, 1, 0, 0, 6, 6, 8, 8, 2, 3, 5, 9],
            [1, 2, 3, 0, 5, 0, 1, 6, 8, 8, 6, 9, 1],
        ),
    ],
)
def test_frequency_sort_correctly_sorts_items_by_frequency(expected: list, items: list):
    assert expected == frequencysort.sort(items)
