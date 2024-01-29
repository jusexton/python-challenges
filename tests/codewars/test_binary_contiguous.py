import pytest

from challenges.codewars import binary_contiguous


@pytest.mark.parametrize(
    "array,expected",
    [
        ([0, 1], 2),
        ([0, 1, 1, 0, 1, 1, 1, 0, 0, 0], 10),
        ([0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 6),
    ],
)
def test_largest_contiguous_equal_sub_array_sum_is_correctly_calculated(
    array: list[int], expected: int
):
    assert binary_contiguous.bin_contiguous(array) == expected
