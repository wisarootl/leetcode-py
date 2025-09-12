import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_ladder_length, run_ladder_length
from .solution import Solution


class TestWordLadder:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "begin_word, end_word, word_list, expected",
        [
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
            ("a", "c", ["a", "b", "c"], 2),
            ("hot", "dog", ["hot", "dog"], 0),
            ("hot", "dog", ["hot", "hog", "dog"], 3),
        ],
    )
    def test_ladder_length(self, begin_word: str, end_word: str, word_list: list[str], expected: int):
        result = run_ladder_length(Solution, begin_word, end_word, word_list)
        assert_ladder_length(result, expected)
