import pytest

from challenges.codewars.stringy import stringy


@pytest.mark.parametrize(
    "size,expected", [(0, ""), (1, "1"), (2, "10"), (3, "101"), (10, "1010101010")]
)
def test_stringy(size: int, expected: str):
    actual = stringy(size)
    assert actual == expected
