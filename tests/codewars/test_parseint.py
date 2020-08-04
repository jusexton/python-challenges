import pytest

from challenges.codewars import parseint


@pytest.mark.parametrize('expected,number_string', [
    (0, 'zero'),
    (1, 'one'),
    (20, 'twenty'),
    (200, 'two hundred'),
    (246, 'two hundred forty-six')
])
def test_number_string_is_correctly_parsed_to_integer_format(expected, number_string):
    assert expected == parseint.parse_int(number_string)
