import pytest

from challenges.codewars import negative


@pytest.mark.parametrize('expected,number', [
    (0, 0),
    (-500, 500),
    (-500, -500)
])
def test_negative_is_correctly_produced(expected, number):
    assert expected == negative.make_negative(number)
