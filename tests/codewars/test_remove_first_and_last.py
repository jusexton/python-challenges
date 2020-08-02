import pytest

from challenges.codewars import remove_first_and_last


@pytest.mark.parametrize('expected,original', [
    ('loquen', 'eloquent'),
    ('ountr', 'country'),
    ('', 'ok')
])
def test_first_and_last_letters_are_removed(expected, original):
    assert expected == remove_first_and_last.remove_first_and_last(original)
