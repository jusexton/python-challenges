import pytest

from challenges.codewars import expansion


@pytest.mark.parametrize('expected,expression', [
    ('ababab', '3(ab)'),
    ('abbbabbb', '2(a3(b))'),
    ('kabaccbaccbacc', 'k(a3(b(a2(c))))')
])
def test_should_correctly_expand_expression(expected: str, expression: str):
    assert expansion.expand(expression) == expected
