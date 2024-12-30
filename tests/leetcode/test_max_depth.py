from challenges.leetcode.max_depth import TreeNode, max_depth


def test_depth_is_zero_when_root_is_none():
    assert 0 == max_depth(None)


def test_finds_max_depth_of_binary_tree():
    root = TreeNode(0, TreeNode(0), TreeNode(0, right=TreeNode(0)))
    assert 3 == max_depth(root)
