import pytest

from challenges.leetcode.is_good import is_good


@pytest.mark.parametrize(
    "expected,array", [(True, [1, 3, 3, 2]), (False, [1, 2]), (False, [2, 4, 4, 4])]
)
def test_correctly_determines_if_array_is_good(expected: bool, array: list[int]):
    actual = is_good(array)
    assert expected is actual
