import pytest

from leetcode_py import logged_test

from .helpers import assert_file_system, run_file_system
from .solution import FileSystem


class TestDesignInMemoryFileSystem:

    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "FileSystem",
                    "ls",
                    "mkdir",
                    "addContentToFile",
                    "ls",
                    "readContentFromFile",
                ],
                [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]],
                [None, [], None, None, ["a"], "hello"],
            ),
            (
                ["FileSystem", "ls", "mkdir", "ls", "mkdir", "ls"],
                [[], ["/"], ["/a"], ["/"], ["/a/b"], ["/"]],
                [None, [], None, ["a"], None, ["a"]],
            ),
            (
                [
                    "FileSystem",
                    "mkdir",
                    "addContentToFile",
                    "ls",
                    "readContentFromFile",
                ],
                [[], ["/x/y"], ["/x/y/z", "content"], ["/x/y"], ["/x/y/z"]],
                [None, None, None, ["z"], "content"],
            ),
            (
                [
                    "FileSystem",
                    "addContentToFile",
                    "readContentFromFile",
                    "addContentToFile",
                    "readContentFromFile",
                ],
                [[], ["/file", "hello"], ["/file"], ["/file", " world"], ["/file"]],
                [None, None, "hello", None, "hello world"],
            ),
            (
                ["FileSystem", "mkdir", "mkdir", "ls", "addContentToFile", "ls"],
                [[], ["/a"], ["/a/b"], ["/a"], ["/a/file", "test"], ["/a"]],
                [None, None, None, ["b"], None, ["b", "file"]],
            ),
            (["FileSystem", "ls"], [[], ["/"]], [None, []]),
            (
                ["FileSystem", "mkdir", "ls", "mkdir", "ls"],
                [[], ["/dir1"], ["/"], ["/dir2"], ["/"]],
                [None, None, ["dir1"], None, ["dir1", "dir2"]],
            ),
            (
                ["FileSystem", "addContentToFile", "ls", "readContentFromFile"],
                [[], ["/root/file", "data"], ["/root"], ["/root/file"]],
                [None, None, ["file"], "data"],
            ),
            (
                [
                    "FileSystem",
                    "mkdir",
                    "addContentToFile",
                    "ls",
                    "readContentFromFile",
                ],
                [
                    [],
                    ["/folder"],
                    ["/folder/doc", "text"],
                    ["/folder"],
                    ["/folder/doc"],
                ],
                [None, None, None, ["doc"], "text"],
            ),
            (
                [
                    "FileSystem",
                    "addContentToFile",
                    "addContentToFile",
                    "readContentFromFile",
                ],
                [[], ["/log", "line1"], ["/log", "line2"], ["/log"]],
                [None, None, None, "line1line2"],
            ),
            (
                ["FileSystem", "mkdir", "mkdir", "mkdir", "ls"],
                [[], ["/a/b/c"], ["/a/b/d"], ["/a/e"], ["/a"]],
                [None, None, None, None, ["b", "e"]],
            ),
            (
                [
                    "FileSystem",
                    "mkdir",
                    "addContentToFile",
                    "addContentToFile",
                    "ls",
                    "readContentFromFile",
                ],
                [
                    [],
                    ["/docs"],
                    ["/docs/readme", "intro"],
                    ["/docs/config", "settings"],
                    ["/docs"],
                    ["/docs/readme"],
                ],
                [None, None, None, None, ["config", "readme"], "intro"],
            ),
        ],
    )
    def test_file_system(
        self,
        operations: list[str],
        inputs: list[list],
        expected: list[str | list[str] | None],
    ):
        result, _ = run_file_system(FileSystem, operations, inputs)
        assert_file_system(result, expected)
