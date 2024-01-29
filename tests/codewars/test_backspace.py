import pytest

from challenges.codewars import backspace


@pytest.mark.parametrize(
    "expected,string", [("ac", "abc#d##c"), ("", "#####"), ("", "abc####d##c#")]
)
def test_clean_string_correctly_applies_backspace_characters(
    expected: str, string: str
):
    assert backspace.clean_string(string) == expected
