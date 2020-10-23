import pytest

from challenges.codewars import removeparentheses


@pytest.mark.parametrize('expected,string', [
    ('exampleexample', 'example(unwanted thing)example'),
    ('a', 'a(b(c))'),
    ('  ', '(first group) (second group) (third group)'),
    ('hello example  something', 'hello example (words(more words) here) something')
])
def test_should_remove_all_characters_surrounded_by_parentheses(expected, string):
    assert removeparentheses.remove_parentheses(string) == expected
