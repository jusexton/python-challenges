import pytest

from challenges.leetcode import simplify_path


@pytest.mark.parametrize(
    "expected,path",
    [
        ("/home/user/Pictures", "/home/user/Documents/../Pictures"),
        ("/", "/../"),
        ("/.../b/d", "/.../a/../b/c/../d/./"),
    ],
)
def test_simplify_path(expected: str, path: str):
    assert expected == simplify_path.simplify_path(path)
