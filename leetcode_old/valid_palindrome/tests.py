import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestValidPalindrome:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True),
            ("", True),
            ("a", True),
            ("Madam", True),
            ("No 'x' in Nixon", True),
            ("Mr. Owl ate my metal worm", True),
        ],
    )
    @logged_test
    def test_is_palindrome(self, s: str, expected: bool):
        result = self.solution.is_palindrome(s)
        assert result == expected
