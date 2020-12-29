import pytest

from challenges.codewars import quarter


@pytest.mark.parametrize("expected,month", [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (4, 10),
    (4, 11),
    (4, 12)
])
def test_correct_quarter_is_returned(expected: int, month: int):
    assert quarter.quarter_of(month) == expected
