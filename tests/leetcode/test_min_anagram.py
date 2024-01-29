import pytest

from challenges.leetcode import min_anagram


@pytest.mark.parametrize(
    "expected,string_one,string_two",
    [
        (0, "test", "tset"),
        (1, "test", "tett"),
        (4, "test", "aaaa"),
        (5, "leetcode", "practice"),
        (4, "friend", "family"),
    ],
)
def test_minimum_number_of_steps_is_returned_to_make_two_strings_anagrams(
    expected: int, string_one: str, string_two: str
):
    assert min_anagram.minimum_steps(string_one, string_two) == expected
