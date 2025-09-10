import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestRansomNote:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "ransom_note, magazine, expected",
        [
            # Original test cases
            ("a", "b", False),
            ("aa", "ab", False),
            ("aa", "aab", True),
            ("aab", "baa", True),
            # Edge cases
            ("", "", True),  # Both empty
            ("", "abc", True),  # Empty ransom note
            ("a", "", False),  # Empty magazine
            ("a", "a", True),  # Single char match
            ("ab", "a", False),  # Ransom longer than magazine
            # More complex cases
            ("abc", "aabbcc", True),  # Multiple of each char
            ("aab", "baa", True),  # Same chars, different order
            ("aaa", "aa", False),  # Not enough of same char
            ("abcd", "dcba", True),  # All different chars
            ("hello", "helloworld", True),  # Ransom is substring
            ("world", "hello", False),  # Missing chars
        ],
    )
    @logged_test
    def test_can_construct(self, ransom_note: str, magazine: str, expected: bool):
        result = self.solution.can_construct(ransom_note, magazine)
        assert result == expected
