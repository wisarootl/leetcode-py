import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_word_break, run_word_break
from .solution import Solution


class TestWordBreak:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
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
            ("aaaaaaa", ["aaaa", "aaa"], True),
            ("aaaaaaa", ["aaaa", "aa"], False),
            ("cars", ["car", "ca", "rs"], True),
            ("raceacar", ["race", "a", "car"], True),
            ("abcdef", ["abc", "def"], True),
            ("abcdef", ["ab", "cd", "ef"], True),
            ("goalspecial", ["go", "goal", "goals", "special"], True),
            ("bb", ["a", "b", "bbb", "bbbb"], True),
        ],
    )
    def test_word_break(self, s: str, word_dict: list[str], expected: bool):
        result = run_word_break(Solution, s, word_dict)
        assert_word_break(result, expected)
