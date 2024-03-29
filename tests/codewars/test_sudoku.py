import pytest

from challenges.codewars.sudoku import Sudoku

TEST_SUDOKU_BOARDS = [
    (
        True,
        Sudoku(
            [
                [7, 8, 4, 1, 5, 9, 3, 2, 6],
                [5, 3, 9, 6, 7, 2, 8, 4, 1],
                [6, 1, 2, 4, 3, 8, 7, 5, 9],
                [9, 2, 8, 7, 1, 5, 4, 6, 3],
                [3, 5, 7, 8, 4, 6, 1, 9, 2],
                [4, 6, 1, 9, 2, 3, 5, 8, 7],
                [8, 7, 6, 3, 9, 4, 2, 1, 5],
                [2, 4, 3, 5, 6, 1, 9, 7, 8],
                [1, 9, 5, 2, 8, 7, 6, 3, 4],
            ]
        ),
    ),
    (True, Sudoku([[1, 4, 2, 3], [3, 2, 4, 1], [4, 1, 3, 2], [2, 3, 1, 4]])),
    (
        False,
        Sudoku(
            [
                [0, 0, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ]
        ),
    ),
    (False, Sudoku([[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3, 4], [1]])),
    (
        False,
        Sudoku(
            [
                [1, 4, 4, 3, "a"],
                [3, 2, 4, 1],
                [4, 1, 3, 3],
                [2, 0, 1, 4],
                ["", False, None, "4"],
            ]
        ),
    ),
    (False, Sudoku([[True]])),
]


@pytest.mark.parametrize("expected,sudoku", TEST_SUDOKU_BOARDS)
def test_sudoku_board_correctly_validates_rows(expected: bool, sudoku: Sudoku):
    assert sudoku.rows_valid() is expected


@pytest.mark.parametrize("expected,sudoku", TEST_SUDOKU_BOARDS)
def test_sudoku_board_correctly_validates_columns(expected: bool, sudoku: Sudoku):
    assert sudoku.columns_valid() is expected


@pytest.mark.parametrize("expected,sudoku", TEST_SUDOKU_BOARDS)
def test_sudoku_board_correctly_validates_blocks(expected: bool, sudoku: Sudoku):
    assert sudoku.blocks_valid() is expected


@pytest.mark.parametrize("expected,sudoku", TEST_SUDOKU_BOARDS)
def test_sudoku_board_correctly_validates_entire_board(expected: bool, sudoku: Sudoku):
    assert sudoku.is_valid() is expected
