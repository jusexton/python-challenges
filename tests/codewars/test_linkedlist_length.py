import pytest

from challenges.codewars.linkedlist_length import Node, length


@pytest.mark.parametrize(
    "node,expected", [(None, 0), (Node(1), 1), (Node(1, Node(1, Node(2))), 3)]
)
def test_correct_length_of_list_is_returned(node: Node, expected: int):
    assert length(node) == expected
