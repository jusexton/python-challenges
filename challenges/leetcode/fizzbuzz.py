from typing import List


def fizzbuzz(value: int) -> List[str]:
    def to_fizzbuzz(v: int) -> str:
        if v % 3 == 0 and v % 5 == 0:
            return 'FizzBuzz'
        if v % 3 == 0:
            return 'Fizz'
        if v % 5 == 0:
            return 'Buzz'

        return str(v)

    return [to_fizzbuzz(i) for i in range(1, value + 1)]
