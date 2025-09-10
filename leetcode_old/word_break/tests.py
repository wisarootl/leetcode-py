import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestWordBreak:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, word_dict, expected",
        [
            ("leetcode", ["leet", "code"], True),
            ("applepenapple", ["apple", "pen"], True),
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
            ("", [], True),
            ("a", ["a"], True),
            ("ab", ["a", "b"], True),
            ("abcd", ["a", "abc", "d"], True),
        ],
    )
    @logged_test
    def test_word_break(self, s: str, word_dict: list[str], expected: bool):
        result = self.solution.word_break(s, word_dict)
        assert result == expected
