import pytest

from challenges.leetcode.shortest_completing_word import shortest_completing_word


@pytest.mark.parametrize('expected,license_plate,words', [
    ('steps', '1s3 PSt', ['step', 'steps', 'stripe', 'stepple']),
    ('pest', '1s3 456', ['looks', 'pest', 'stew', 'show'])
])
def test_shortest_completing_string_is_correctly_returned(
    expected: str,
    license_plate: str,
    words: list[str]
):
    actual = shortest_completing_word(license_plate, words)
    assert expected == actual
