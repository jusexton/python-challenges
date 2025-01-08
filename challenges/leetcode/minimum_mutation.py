from collections import deque


def min_mutation(self, start: str, end: str, bank: list[str]) -> int:
    def differ_by_one(a, b):
        return sum(1 for i in range(len(a)) if a[i] != b[i]) == 1

    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        curr, mutations = queue.popleft()
        if curr == end:
            return mutations

        for neighbor in bank:
            if neighbor not in visited and differ_by_one(curr, neighbor):
                visited.add(neighbor)
                queue.append((neighbor, mutations + 1))

    return -1
