from challenges.leetcode.nearest_exit import nearest_exit


def test_finds_nearest_exit_out_of_maze():
    assert 1 == nearest_exit(
        [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
    )

    assert 2 == nearest_exit(
        [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]
    )

    assert 12 == nearest_exit(
        [
            ["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", ".", "+"],
        ],
        [0, 1],
    )
