from typing import List

import pytest

from challenges.leetcode import unique_email


@pytest.mark.parametrize('expected,emails', [
    (0, []),
    (2, [
        'test.email+alex@leetcode.com',
        'test.e.mail+bob.cathy@leetcode.com',
        'testemail+david@lee.tcode.com'
    ])
])
def test_correct_number_of_emails_is_returned(expected: int, emails: List[str]):
    assert unique_email.unique_email_count(emails) == expected
