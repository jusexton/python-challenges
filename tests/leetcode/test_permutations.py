import pytest

from challenges.leetcode import permutations


@pytest.mark.parametrize('expected,numbers', [(
        [[1, 2, 3],
         [1, 3, 2],
         [2, 1, 3],
         [2, 3, 1],
         [3, 1, 2],
         [3, 2, 1]], [1, 2, 3])]
                         )
def test_should_return_all_permutations(expected, numbers):
    for expected_permutation, actual_permutation in zip(expected, permutations.permute(numbers)):
        assert list(expected_permutation) == list(actual_permutation)
