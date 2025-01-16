from challenges.leetcode.col_row_pairs import equal_pairs


def test_row_and_col_pairs_are_counted():
    assert 3 == equal_pairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
