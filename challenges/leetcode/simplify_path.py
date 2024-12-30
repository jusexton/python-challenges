# https://leetcode.com/problems/simplify-path
# Tags: Stack, String


def simplify_path(path: str) -> str:
    stack = []
    segments = path.split("/")
    for segment in segments:
        if segment != "" and segment != ".":
            if segment == ".." and stack:
                stack.pop()
            elif segment != "..":
                stack.append(segment)

    return "/" + "/".join(stack)
