import pytest

from challenges.codewars import npower


@pytest.mark.parametrize('expected,array,index', [
    (1, [1], 0),
    (2, [1, 2, 3], 1),
    (9, [1, 2, 3], 2)
])
def test_nth_power_returns_nth_power_of_nth_index(expected, array, index):
    assert npower.nth_power(array, index) == expected


def test_nth_power_returns_negative_one_when_n_is_out_of_range():
    assert npower.nth_power([1, 2], 5) == -1
