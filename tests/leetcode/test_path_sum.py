from challenges.leetcode.path_sum import TreeNode, has_path_sum


def test_identifies_when_path_sum_can_be_calculated():
    root = TreeNode(
        1, TreeNode(5, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(12), TreeNode(3))
    )
    assert has_path_sum(root, 8)
