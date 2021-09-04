import pytest

from challenges.codewars import need_one


@pytest.mark.parametrize('sequence,value,expected', [
    ([1, 2, 3], 2, True),
    (['come', 'on', 110, '2500', 10, '!', 7, 15], 'Come', False)
])
def test_check_correctly_finds_given_value_in_given_list(sequence: list, value, expected: bool):
    assert need_one.check(sequence, value) is expected
