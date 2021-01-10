import pytest

from challenges.codewars import move_zeroes


@pytest.mark.parametrize('arr,expected', [
    ([], []),
    ([0, "a"], ["a", 0]),
    ([1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
    ([0, 1, None, 2, False, 1, 0], [1, None, 2, False, 1, 0, 0]),
    (["a"], ["a"])
])
def test_zeroes_are_moved_to_end_of_array(arr: list, expected: list):
    assert move_zeroes.move_zeroes(arr) == expected
