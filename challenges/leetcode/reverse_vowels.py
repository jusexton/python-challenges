# def reverse_vowels(s: str) -> str:
#     vowels = [c for c in s if c.lower() in ("a", "e", "i", "o", "u")]
#     res = []
#     for c in s:
#         if c.lower() in ("a", "e", "i", "o", "u"):
#             res.append(vowels.pop())
#         else:
#             res.append(c)
#     return "".join(res)


def reverse_vowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1
        if left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(s)
