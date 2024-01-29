import pytest

from challenges.other.dfsearch import search, TreeNode


@pytest.mark.parametrize(
    "tree,expected",
    [
        (TreeNode(data=1, nodes=[TreeNode(2), TreeNode(3)]), [1, 2, 3]),
        (
            TreeNode(
                data=1,
                nodes=[
                    TreeNode(2, nodes=[TreeNode(3), TreeNode(4)]),
                    TreeNode(5, nodes=[TreeNode(6), TreeNode(7)]),
                ],
            ),
            [1, 2, 3, 4, 5, 6, 7],
        ),
    ],
)
def test_depth_first_search(tree: TreeNode, expected: int):
    assert search(tree) == expected
