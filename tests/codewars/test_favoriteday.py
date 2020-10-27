from typing import List

import pytest

from challenges.codewars import favoriteday


@pytest.mark.parametrize('expected,year', [
    (['Friday'], 2427),
    (['Saturday'], 2185),
    (['Monday'], 1770),
    (['Monday', 'Sunday'], 1984),
    (['Saturday', 'Sunday'], 2000)
])
def test_should_collect_the_most_common_days_of_the_week_from_a_given_year(expected: List[str], year: int):
    assert favoriteday.most_frequent_days(year) == expected
