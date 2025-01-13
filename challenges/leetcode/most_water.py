import sys


def max_area(heights: list[int]) -> int:
    max_area = -sys.maxsize
    left, right = 0, len(heights) - 1
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, area)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return max_area
