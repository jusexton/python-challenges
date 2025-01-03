import heapq


def find_kth_largest(numbers: list[int], k: int) -> int:
    heap = numbers[:k]
    heapq.heapify(heap)

    for number in numbers[k:]:
        if number > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, number)

    return heap[0]
