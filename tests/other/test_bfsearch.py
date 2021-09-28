import pytest

from challenges.other.bfsearch import search, TreeNode


@pytest.mark.parametrize('tree,expected', [
    (TreeNode(
        data=1,
        left=TreeNode(2),
        right=TreeNode(3)
    ), [1, 2, 3]),
    (TreeNode(
        data=1,
        left=TreeNode(
            2,
            left=TreeNode(4),
            right=TreeNode(5)),
        right=TreeNode(
            3,
            left=TreeNode(6),
            right=TreeNode(7))
    ), [1, 2, 3, 4, 5, 6, 7])
])
def test_breadth_first_search(tree: TreeNode, expected: int):
    assert search(tree) == expected
