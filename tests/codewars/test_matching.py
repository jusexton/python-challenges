import pytest

from challenges.codewars import matching


@pytest.mark.parametrize(
    "pattern,s",
    [
        ("code*s", "codewars"),
        ("codewar*s", "codewars"),
        ("c", "c"),
        ("*s", "codewars"),
        ("*s", "s"),
        ("s*", "s"),
        ("aa*", "aaa"),
        ("*", "codewars"),
    ],
)
def test_is_matching_correctly_identifies_strings_that_match_given_pattern(
    pattern: str, s: str
):
    assert matching.is_match(pattern, s) is True


@pytest.mark.parametrize(
    "pattern,s",
    [
        ("code*warrior", "codewars"),
        ("aa", "aaa"),
        ("aaa", "aa"),
        ("aaa*", "aa"),
    ],
)
def test_is_matching_correctly_identifies_strings_that_do_not_match_given_pattern(
    pattern: str, s: str
):
    assert matching.is_match(pattern, s) is False
