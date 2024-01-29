import pytest

from challenges.codewars import century


@pytest.mark.parametrize(
    "year,expected_century",
    [
        ("2011", "21st"),
        ("2154", "22nd"),
        ("2259", "23rd"),
        ("1234", "13th"),
        ("1023", "11th"),
        ("2000", "20th"),
    ],
)
def test_get_century_yields_correct_century_from_given_year(
    year: str, expected_century: str
):
    assert century.get_century(year) == expected_century
