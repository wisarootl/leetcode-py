import pytest

from leetcode_py import logged_test

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
            ("Was it a car or a cat I saw?", True),
            ("Madam, I'm Adam", True),
            ("Never odd or even", True),
            ("Do geese see God?", True),
            ("Step on no pets", True),
            ("12321", True),
            ("hello", False),
            ("ab", False),
        ],
    )
    def test_is_palindrome(self, s: str, expected: bool):
        result = run_is_palindrome(Solution, s)
        assert_is_palindrome(result, expected)
