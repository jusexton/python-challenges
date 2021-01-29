import pytest

from challenges.codewars import message_validator


@pytest.mark.parametrize('message,expected', [
    ('', True),
    ('3hey5hello2hi', True),
    ('4code13hellocodewars', True),
    ('3hey5hello2hi5', False),
    ('code4hello5', False),
    ('1a2bb3ccc4dddd5eeeee', True),
    ('10aaaaaaaaaa', True),
    ('a1', False),
    ('7XGZPUPH11IURHKHKGCTF', True)
])
def test_returns_correct_validity_of_given_message(message: str, expected: bool):
    assert message_validator.is_a_valid_message(message) == expected
