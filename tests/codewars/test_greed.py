import pytest

from challenges.codewars import greed


@pytest.mark.parametrize('expected,dice', [
    (0, []),
    (1200, [1, 1, 1, 1, 1]),
    (250, [5, 1, 3, 4, 1]),
    (450, [2, 4, 4, 5, 4]),
    (600, [6, 6, 6, 3, 3])
])
def test_should_return_correctly_calculated_score(expected, dice):
    assert expected == greed.calculate_score(dice)
