import itertools
import math
from typing import List


def is_perfect_square(number: int):
    return math.sqrt(number) ** 2 == number


class Sudoku(object):
    def __init__(self, data: List[List[int]]):
        self.data = data
        self.size = len(data)

    def is_valid(self):
        return self.rows_valid() and self.columns_valid() and self.blocks_valid()

    def rows_valid(self):
        for row in self.data:
            valid_row = self._valid_group(row)
            if not valid_row:
                return False

        return True

    def columns_valid(self):
        for column in range(0, self.size):
            try:
                column_numbers = [self.data[column][row] for row in range(0, self.size)]
                valid_column = self._valid_group(column_numbers)
                if not valid_column:
                    return False
            except IndexError:
                return False

        return True

    def blocks_valid(self):
        block_size = int(math.sqrt(self.size))
        for i in range(0, self.size, block_size):
            for j in range(0, self.size, block_size):
                square_rows = [row[j:j + block_size] for row in self.data[i:i + block_size]]
                square = list(itertools.chain.from_iterable(square_rows))
                valid_block = self._valid_group(square)
                if not valid_block:
                    return False

        return True

    def _valid_group(self, numbers: List[int]):
        try:
            number_set = set(numbers)
            not_boolean = all(not isinstance(number, bool) for number in numbers)
            in_range = all(number in range(1, self.size + 1) for number in numbers)
            valid_size = len(number_set) == self.size
            valid_sum = sum(numbers) == sum(number_set)
            perfect_square = is_perfect_square(len(number_set))
            return valid_size and valid_sum and perfect_square and in_range and not_boolean
        except TypeError:
            return False
