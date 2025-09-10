import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestWordLadder:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "begin_word, end_word, word_list, expected",
        [
            # Basic cases
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
            ("a", "c", ["a", "b", "c"], 2),
            # Edge cases
            ("hot", "dog", ["hot", "dog"], 0),  # No intermediate words
            ("hot", "hot", ["hot"], 1),  # Same word
            ("cat", "dog", [], 0),  # Empty word list
            ("cat", "dog", ["cat"], 0),  # End word not in list
            # Single character changes
            ("a", "b", ["a", "b"], 2),
            ("ab", "cd", ["ab", "ad", "cd"], 3),
            # Longer paths
            ("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"], 4),
            # Multiple possible paths (should return shortest)
            ("cat", "dog", ["cat", "bat", "bag", "dag", "dog", "cag", "cog"], 4),
            # No path exists
            ("abc", "def", ["abc", "def", "ghi"], 0),
            # Direct transformation
            ("cat", "bat", ["cat", "bat"], 2),
            # Longer word length
            ("word", "form", ["word", "worm", "form", "foam", "flam", "flab"], 3),
        ],
    )
    @logged_test
    def test_ladder_length(self, begin_word: str, end_word: str, word_list: list[str], expected: int):
        result = self.solution.ladder_length(begin_word, end_word, word_list)
        assert result == expected
