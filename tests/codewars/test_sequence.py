import pytest

from challenges.codewars import sequence


@pytest.mark.parametrize('expected,values', [
    (True, [1, 2, 3]),
    (True, [10, 11, 12, 13, 14, 15, 16]),
    (True, [1, 3, 5, 7]),
    (True, [3, 6, 9, 12, 15]),
    (False, [11, 4, 2, 1]),
    (False, [12, 5, 34, 87, 13, 1, 5, 6, 7, 8, 12]),
    (False, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
])
def test_should_return_correct_when_given_certain_value(expected, values):
    assert sequence.validate(values) is expected
