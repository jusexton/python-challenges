# def hamming_weight(self, n: int) -> int:
#     return n.bit_count()


def hamming_weight(self, n: int) -> int:
    return bin(n)[2:].count("1")


# def hamming_weight(self, n: int) -> int:
#     count = 0
#     while n > 0:
#         if n & 1 == 1:
#             count += 1
#         n >>= 1

#     return count
