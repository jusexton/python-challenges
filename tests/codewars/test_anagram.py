import pytest

from challenges.codewars import anagrams


@pytest.mark.parametrize('expected,test,original', [
    (True, 'Creative', 'Reactive'),
    (True, 'foefet', 'toffee'),
    (True, 'Twoo', 'WooT'),
    (False, 'dumble', 'bumble'),
    (False, 'apple', 'pale')
])
def test_anagrams_are_correctly_identified(expected, test, original):
    assert expected == anagrams.is_anagram(test, original)
