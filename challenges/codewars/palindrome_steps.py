def palindrome_chain_length(n: int) -> int:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    count = 0
    while not is_palindrome(str(n)):
        n += int(str(n)[::-1])
        count += 1

    return count

