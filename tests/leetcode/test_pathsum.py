import pytest

from challenges.leetcode import pathsum


@pytest.fixture
def test_tree() -> pathsum.TreeNode:
    root_left = pathsum.TreeNode(4)
    root_left.right = pathsum.TreeNode(7)

    root_right = pathsum.TreeNode(3)
    root_right.right = pathsum.TreeNode(6)

    populated_test_tree = pathsum.TreeNode(2)
    populated_test_tree.left = root_left
    populated_test_tree.right = root_right

    return populated_test_tree


@pytest.mark.parametrize("expected", [11, 13])
def test_should_return_true_when_tree_contains_requested_sum(
    expected: int, test_tree: pathsum.TreeNode
):
    result = pathsum.path_sum_exists(test_tree, expected)
    assert result is True


@pytest.mark.parametrize("expected", [0, 1, 2, 5, 6])
def test_should_return_false_when_tree_contains_requested_sum(
    expected: int,
    test_tree: pathsum.TreeNode,
):
    result = pathsum.path_sum_exists(test_tree, expected)
    assert result is False
