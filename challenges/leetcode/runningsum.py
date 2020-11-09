from typing import List


def running_sum(numbers: List[int]) -> List[int]:
    if len(numbers) == 0:
        return [0]

    running = 0
    result = []
    for number in numbers:
        running += number
        result.append(running)

    return result
