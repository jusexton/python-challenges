import pytest

from challenges.leetcode.k_set_bits import k_set_bits


@pytest.mark.parametrize(
    "expected,numbers,k", [(13, [5, 10, 1, 5, 2], 1), (1, [4, 3, 2, 1], 2)]
)
def test_sums_values_at_index_that_match_given_bit_count(
    expected: int, numbers: list[int], k: int
):
    actual = k_set_bits(numbers, k)
    assert actual == expected
