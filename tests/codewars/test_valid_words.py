import pytest

from challenges.codewars.valid_words import valid_word_count


@pytest.mark.parametrize('s,expected', [
    ('cat and  dog', 3),
    ('!this  1-s b8d!', 0),
    ('alice and  bob are playing stone-game10', 5),
    ('. ! 7hk  al6 l! aon49esj35la k3 7u2tkh  7i9y5  !jyylhppd et v- h!ogsouv 5', 4)
])
def test_valid_word_count(s: str, expected: int):
    actual = valid_word_count(s)
    assert actual == expected
