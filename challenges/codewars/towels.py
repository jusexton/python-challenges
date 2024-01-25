def sort_the_pile(towels: list[str], used: list[int]) -> list[str]:
    for use in used:
        remaining = len(towels) - use
        used_towels = towels[remaining : len(towels)]
        towels = towels[0:remaining]
        towels.extend(sorted(used_towels, reverse=True))

    return towels
