import pytest

from challenges.codewars import fibonacci


@pytest.mark.parametrize('n,expected', [
    (-1, []),
    (0, []),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
])
def test_fibonacci_sequence_is_generated_correctly(n: int, expected: list[int]):
    assert fibonacci.fibonacci(n) == expected
