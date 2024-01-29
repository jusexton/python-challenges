import pytest

from challenges.codewars import population_growth


@pytest.mark.parametrize(
    "expected,p0,percent,aug,p",
    [
        (15, 1500, 5, 100, 5000),
        (10, 1500000, 2.5, 10000, 2000000),
        (94, 1500000, 0.25, 1000, 2000000),
    ],
)
def test_nb_year_yields_correct_results(expected, p0, percent, aug, p):
    assert population_growth.nb_year(p0, percent, aug, p) == expected
