import pytest

from challenges.codewars import charfreq


@pytest.mark.parametrize('expected,value', [
    ('c:**,h:*,i:*,a:*,g:*,o:*', 'Chicago'),
    ('b:*,a:*,n:*,g:*,k:**,o:*', 'Bangkok'),
    ('l:*,a:**,s:**,v:*,e:*,g:*', 'Las Vegas')
])
def test_character_frequency_string_is_correctly_generated(expected: str, value: str):
    assert expected == charfreq.character_freq(value)
