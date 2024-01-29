import pytest

from challenges.codewars import repeating


@pytest.mark.parametrize(
    "expected,string",
    [
        ("", ""),
        ("e", "test"),
        ("h", "hello"),
        ("c", "code wars"),
        (",", "Go hang a salami, I'm a lasagna hog!"),
        ("T", "sTreSS"),
    ],
)
def test_should_return_the_first_non_repeating_character(expected, string):
    assert expected == repeating.first_non_repeating_letter(string)


@pytest.mark.parametrize(
    "string",
    [
        "TT",
        "testtest",
    ],
)
def test_should_return_empty_string_when_all_characters_repeat(string):
    assert "" == repeating.first_non_repeating_letter(string)
