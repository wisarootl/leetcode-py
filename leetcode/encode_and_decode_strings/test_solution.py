import pytest

from leetcode_py import logged_test

from .helpers import assert_encode_decode, run_encode_decode
from .solution import Solution


class TestEncodeAndDecodeStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs",
        [
            ["Hello", "World"],
            ["abc", "def"],
            [""],
            ["a", "b", "c"],
            ["", "", ""],
            ["hello", "", "world"],
            ["a#b", "c#d"],
            ["4#3hello", "world"],
            ["#", "##", "###"],
            ["abc123", "def456", "ghi789"],
            ["special!@#$%^&*()"],
            ["with spaces", "and tabs\t", "and newlines\n"],
            ["unicode测试", "emoji😀"],
            ["very long string " * 10],
            ["a" * 200],
            [],
            ["single"],
            ["comma,separated", "values,here"],
            ["pipe|separated", "values|here"],
            ["colon:separated", "values:here"],
        ],
    )
    def test_encode_decode(self, strs: list[str]):
        result = run_encode_decode(Solution, strs)
        assert_encode_decode(result, strs)
