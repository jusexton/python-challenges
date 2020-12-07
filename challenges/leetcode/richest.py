from typing import List


def richest_customer(accounts: List[List[int]]) -> int:
    return max(sum(account) for account in accounts)
