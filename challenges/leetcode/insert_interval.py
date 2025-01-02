def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    i = 0
    updated = []
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        updated.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    updated.append(new_interval)

    while i < len(intervals):
        updated.append(intervals[i])
        i += 1
    return updated
