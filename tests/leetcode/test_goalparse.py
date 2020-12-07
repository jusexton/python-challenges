import pytest

from challenges.leetcode import goalparse


@pytest.mark.parametrize('expected,text', [
    ('', ''),
    ('Goal', 'G()(al)'),
    ('Gooooal', 'G()()()()(al)'),
    ('alGalooG', '(al)G(al)()()G'),
])
def test_returns_correctly_interpreted_text(expected: str, text: str):
    assert goalparse.interpret(text) == expected
