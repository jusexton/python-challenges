import pytest

from challenges.codewars.mathdsl import divided_by, nine, plus, three, times, two, zero


@pytest.mark.parametrize(
    "expected,actual", [(5, two(plus(three()))), (27, zero(plus(three(times(nine())))))]
)
def test_should_correctly_perform_calculations(expected, actual):
    assert expected == actual


def test_should_raise_arithmetic_error_when_dividing_by_zero():
    with pytest.raises(ArithmeticError):
        two(divided_by(zero()))
