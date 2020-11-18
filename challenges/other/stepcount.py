# Problem: Given x number of stairs, a boy can jump 1 2 or 3 steps. Return how many different combinations
# the boy can jump the stairs.

# First attempt. Was very slow but I added caching in the next solution and it improved performance 10 fold.
# def step_count(stair_count: int) -> int:
#     if stair_count == 1:
#         return 1
#     elif stair_count == 2:
#         return 2
#     else:
#         return step_count(stair_count - 1) + step_count(stair_count - 2) + step_count(stair_count - 3)


import functools


@functools.lru_cache(maxsize=None)
def step_count(stair_count: int) -> int:
    if stair_count < 4:
        state_cycles = [1, 2, 4]
        return state_cycles[stair_count - 1]
    else:
        return step_count(stair_count - 1) + step_count(stair_count - 2) + step_count(stair_count - 3)
