import pytest

from challenges.codewars import summultiples


@pytest.mark.parametrize('expected,number', [
    (0, 0),
    (8, 5),
    (33, 10)
])
def test_should_return_sum_of_all_number_divisible_by_three_and_five(expected, number):
    assert expected == summultiples.sum_multiples(number)
