import pytest

from challenges.codewars import pyramid_array


@pytest.mark.parametrize('expected,n', [
    ([], 0),
    ([[1]], 1),
    ([[1], [1, 1]], 2)
])
def test_should_return_false_when_given_prime_number(expected, n):
    assert pyramid_array.pyramid(n) == expected
