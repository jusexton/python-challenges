from typing import List

import pytest

from challenges.codewars import animal_years


@pytest.mark.parametrize('human_years,expected', [
    (1, [1, 15, 15],),
    (10, [10, 56, 64],)
])
def test_that_animal_years_are_correctly_returned(human_years: int, expected: List[int]):
    assert animal_years.human_years_cat_years_dog_years(human_years) == expected
