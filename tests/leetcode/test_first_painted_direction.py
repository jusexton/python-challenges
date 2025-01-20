from challenges.leetcode.first_painted_direction import first_complete_index


def test_first_painted_direction_returns_index():
    assert 2 == first_complete_index([1, 3, 4, 2], [[1, 4], [2, 3]])
    assert 1 == first_complete_index([1, 4, 5, 2, 6, 3], [[4, 3, 5], [1, 2, 6]])
