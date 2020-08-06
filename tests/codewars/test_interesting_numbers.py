import pytest

from challenges.codewars import interesting_numbers


@pytest.mark.parametrize('expected,number,awesome_phrases', [
    (2, 100, []),
    (2, 111, []),
    (2, 1337, [1337]),
    (2, 999999, []),
    (2, 12321, []),
    (2, 12345, []),
    (2, 234567890, []),
    (2, 1234567890, []),
    (2, 43210, []),
    (2, 87654, []),
    (1, 120, []),
    (1, 98, []),
    (1, 99, []),
    (1, 110, []),
    (1, 9998, []),
    (1, 87653, []),
    (1, 1336, [1337]),
    (1, 11209, []),
    (0, 1337, []),
])
def test_interesting_numbers_are_correctly_determined(expected, number, awesome_phrases):
    assert interesting_numbers.is_interesting(number, awesome_phrases) == expected
