import pytest

from challenges.leetcode import fizzbuzz


@pytest.mark.parametrize('expected,value', [
    ([
         '1',
         '2',
         'Fizz',
         '4',
         'Buzz',
         'Fizz',
         '7',
         '8',
         'Fizz',
         'Buzz',
         '11',
         'Fizz',
         '13',
         '14',
         'FizzBuzz'
     ], 15)
])
def test_correct_fizz_buzz_values_are_returned(expected, value):
    assert fizzbuzz.fizzbuzz(value) == expected
