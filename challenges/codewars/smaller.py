# Kyu 7
# def smaller(arr: list[int]) -> list[int]:
#     return [
#         sum(number < arr[i] for number in arr[i:]) for i in range(0, len(arr))
#     ]


# Kyu 3
def smaller(arr):
    result = [0] * len(arr)
    root, index = None, len(arr) - 1
    while index >= 0:
        root = tree(root, index, arr[index], 0, result)
        index -= 1
    return result


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.count = 0
        self.occurrences = 1


def tree(root, index, num, sumation, result):
    if root is None:
        result[index] = sumation
        return Node(num)
    if root.value == num:
        root.occurrences += 1
        result[index] = sumation + root.count
    elif root.value > num:
        root.count += 1
        root.left = tree(root.left, index, num, sumation, result)
    else:
        count = sumation + root.count + root.occurrences
        root.right = tree(root.right, index, num, count, result)
    return root
