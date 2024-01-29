import pytest

from challenges.codewars import numberstrings


@pytest.mark.parametrize(
    "expected,string",
    [(695, "gh12cdy695m1"), (9, "2ti9iei7qhr5"), (61, "vih61w8oohj5")],
)
def test_number_strings_correctly_returns_the_largest_number_in_given_string(
    expected: int, string: str
):
    assert expected == numberstrings.solve(string)
