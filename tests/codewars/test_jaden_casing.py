import pytest

from challenges.codewars.jaden_casing import to_jaden_case


@pytest.mark.parametrize('s,expected', [
    ('', ''),
    ('test', 'Test'),
    ('Test', 'Test'),
    ('test test', 'Test Test')
])
def test_to_jaden_case(s: str, expected: str):
    actual = to_jaden_case(s)
    assert actual == expected
