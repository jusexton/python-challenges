import pytest

from challenges.codewars import prime


@pytest.mark.parametrize(
    "number",
    [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        23,
    ],
)
def test_should_return_true_when_given_prime_number(number):
    assert prime.is_prime(number) is True


@pytest.mark.parametrize(
    "number",
    [
        -1,
        4,
        6,
    ],
)
def test_should_return_false_when_given_prime_number(number):
    assert prime.is_prime(number) is False
