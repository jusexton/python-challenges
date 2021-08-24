import pytest

from challenges.codewars import reverse_words


@pytest.mark.parametrize('s,expected', [
    ('test words', 'words test')
])
def test_words_are_correctly_reversed(s: str, expected: str):
    assert expected == reverse_words.reverse_words(s)
