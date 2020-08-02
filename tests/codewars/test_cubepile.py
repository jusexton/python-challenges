import pytest

from challenges.codewars import cubepile


@pytest.mark.parametrize('expected,m', [
    (1, 1),
    (2022, 4183059834009),
    (-1, 24723578342962),
    (4824, 135440716410000),
    (3568, 40539911473216),
    (3218, 26825883955641)
])
def test_tower_height_is_correctly_calculated(expected, m):
    assert expected == cubepile.find_nb(m)
