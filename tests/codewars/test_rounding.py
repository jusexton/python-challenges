import pytest

from challenges.codewars import rounding


@pytest.mark.parametrize("expected,number", [(0, 0), (25, 22), (30, 30)])
def test_should_return_the_next_multiple_of_five(expected, number):
    assert expected == rounding.multiple_of_five(number)
