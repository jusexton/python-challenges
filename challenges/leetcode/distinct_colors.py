from collections import defaultdict


def query_results(_: int, queries: list[list[int]]) -> list[int]:
    results = []
    balls = {}
    colors = defaultdict(int)
    for x, y in queries:
        if x in balls:
            curr_color = balls[x]
            if colors[curr_color] == 1:
                del colors[curr_color]
            else:
                colors[curr_color] -= 1

        balls[x] = y
        colors[y] += 1
        results.append(len(colors))

    return results
