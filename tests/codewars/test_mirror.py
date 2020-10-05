from typing import List

import pytest

from challenges.codewars import mirror


@pytest.mark.parametrize('expected,items', [
    ([1], [1]),
    ([1, 2, 1], [2, 1]),
    ([1, 2, 1], [1, 2]),
    ([-16, -8, 0, 18, 42, 18, 0, -8, -16], [-8, 42, 18, 0, -16])
])
def test_mirror_correctly_returns_mirrored_items_of_given_items(expected: List[int], items: List[int]):
    assert expected == mirror.mirror(items)
