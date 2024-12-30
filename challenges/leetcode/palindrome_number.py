# https://leetcode.com/problems/palindrome-number/
# Tags: Math


def is_palindrome(x: int) -> bool:
    num_str = str(x)
    return num_str == num_str[::-1]
