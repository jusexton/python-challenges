from collections import Counter


def sort(items: list) -> list:
    counter = Counter(items)
    return sorted(items, key=lambda k: (-counter[k], k))


# Original solution
# def sort(items: list) -> list:
#     sorted_counter = sorted(sorted(Counter(items).items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
#     result = []
#     for k, v in sorted_counter:
#         result += [k] * v
#
#     return result
