import pytest

from challenges.leetcode import dayofweek


@pytest.mark.parametrize(
    "expected,day,month,year",
    [
        ("Saturday", 31, 8, 2019),
        ("Tuesday", 8, 12, 2020),
        ("Monday", 7, 12, 2020),
        ("Sunday", 6, 12, 2020),
        ("Sunday", 18, 7, 1999),
    ],
)
def test_should_return_correct_day_of_week(expected, day, month, year):
    assert dayofweek.day_of_the_week(day, month, year) == expected
