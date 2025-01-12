def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
    max_candies = max(candies)
    return [count + extra_candies >= max_candies for count in candies]
