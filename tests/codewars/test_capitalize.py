import pytest

from challenges.codewars import capitalize


@pytest.mark.parametrize('expected,paragraph', [
    ('Test sentence', 'test sentence'),
    ('This sentence. Should be. Correctly capitalized.',
     'this sentence. should be. correctly capitalized.')
])
def test_sentences_in_given_paragraph_are_capitalized(expected: str, paragraph: str):
    assert expected == capitalize.capitalize_sentences(paragraph)
