from typing import List

import pytest

from challenges.codewars import socialgolfer


@pytest.mark.parametrize('expected,input', [
    (True, [
        ["AB", "CD"],
        ["AD", "BC"],
        ["BD", "AC"]
    ]),
    (True, [
        ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
        ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
        ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
        ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
        ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']
    ]),
    (False, [
        ["AB", "CD", "EF", "GH"],
        ["AC", "BD", "EG", "FH"],
        ["AD", "CE"],
        ["AE", "BG", "CH", "FD"]
    ]),
    (False, [
        ["ABC", "DEF"],
        ["ADE", "CBF"]
    ])
])
def test_golf_schedule_is_valid(expected: bool, input: List[List[str]]):
    assert socialgolfer.valid(input) is expected
