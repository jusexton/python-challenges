from collections import namedtuple

from challenges.leetcode.binarysearch import TreeNode, search


def test_returns_subtree_of_given_found_value():
    one = TreeNode(1)
    three = TreeNode(3)
    two = TreeNode(2, one, three)

    five = TreeNode(5)
    seven = TreeNode(7)
    six = TreeNode(6, five, seven)

    root = TreeNode(4, two, six)

    TestCase = namedtuple("TestCase", "expected,val")
    test_cases = [
        TestCase(expected=root, val=4),
        TestCase(expected=three, val=3),
        TestCase(expected=five, val=5),
    ]

    for test in test_cases:
        result = search(root, test.val)
        assert result is not None
        assert result == test.expected
