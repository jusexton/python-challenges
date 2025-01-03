def search_insert(numbers: list[int], target: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (right - left // 2) + left
        if numbers[mid] == target:
            return mid
        elif target > numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left
