import pytest

from challenges.codewars import sharedbit


@pytest.mark.parametrize("expected,a,b", [
    (False, 1, 2),
    (False, 16, 8),
    (False, 1, 1),
    (False, 2, 3),
    (False, 7, 10),
    (True, 43, 77),
    (True, 7, 15),
    (True, 23, 7)
])
def test_shared_bits_are_identified(expected: bool, a: int, b: int):
    assert sharedbit.shared_bits(a, b) == expected
