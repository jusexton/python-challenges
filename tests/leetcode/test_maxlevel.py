import pytest

from challenges.leetcode.maxlevel import TreeNode, max_level_sum


@pytest.mark.parametrize('expected,root', [
    (1, TreeNode()),
    (1, TreeNode(10, TreeNode(5), TreeNode(4))),
    (2, TreeNode(0, TreeNode(10), TreeNode(2))),
    (2, TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode())),
])
def test_returns_level_with_maximum_sum(expected: int, root: TreeNode):
    assert max_level_sum(root) == expected
