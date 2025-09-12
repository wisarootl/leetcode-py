import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_is_palindrome, run_is_palindrome
from .solution import Solution


class TestValidPalindrome:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
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
    def test_is_palindrome(self, s: str, expected: bool):
        result = run_is_palindrome(Solution, s)
        assert_is_palindrome(result, expected)
