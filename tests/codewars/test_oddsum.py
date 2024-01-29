import pytest

from challenges.codewars import oddsum


@pytest.mark.parametrize("expected,number", [(1, 1), (8, 2), (2197, 13), (6859, 19)])
def test(expected, number):
    assert expected == oddsum.row_sum_odd_numbers(number)
