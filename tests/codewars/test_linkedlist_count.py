import pytest

from challenges.codewars.linkedlist_count import Node, count


@pytest.mark.parametrize('node,data,expected', [
    (None, 0, 0),
    (Node(1), 1, 1),
    (Node(1, Node(1, Node(2))), 1, 2),
    (Node(1, Node(2, Node(3))), 2, 1)
])
def test_correct_count_of_elements_is_returned(node: Node, data: int, expected: int):
    assert count(node, data) == expected
