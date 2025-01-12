def gcd_of_strings(str1: str, str2: str) -> str:
    i = 0
    while str1[i] == str2[i]:
        i += 1
    return str1[:i]
