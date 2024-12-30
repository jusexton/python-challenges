from challenges.leetcode.same_tree import TreeNode, is_same_tree


def test_identifies_when_two_trees_are_same():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(root, root)


def test_identifies_when_two_trees_are_not_same():
    p_root = TreeNode(1, left=TreeNode(2))
    q_root = TreeNode(1, right=TreeNode(2))
    assert not is_same_tree(p_root, q_root)
