import pytest

from challenges.codewars.vowel_count import vowel_count


@pytest.mark.parametrize('s,expected', [
    ('', 0),
    ('abc', 1),
    ('aeiou', 5),
    ('nhrt', 0)
])
def test_vowels_are_counted_correctly(s: str, expected: int):
    actual = vowel_count(s)
    assert actual == expected
