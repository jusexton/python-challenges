import pytest

from challenges.codewars import oddoccurrence


@pytest.mark.parametrize('expected,values', [
    (2, [1, 2, 2, 2, 1]),
    (5, [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]),
    (-1, [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
])
def test_should_return_the_int_that_occurs_an_odd_number_of_times_in_the_sequence(expected, values):
    assert expected == oddoccurrence.odd_occurrence(values)
