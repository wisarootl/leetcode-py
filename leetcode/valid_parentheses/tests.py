import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestValidParentheses:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, expected",
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([])", True),
            ("([)]", False),
            ("", True),
            ("(", False),
            (")", False),
            ("{[()]}", True),
            ("{[(])}", False),
            ("(((", False),
            (")))", False),
            ("()()()", True),
            ("({[]})", True),
            ("({[}])", False),
            ("[[[[[]]]]]", True),
            ("[[[[[]]]]", False),
            ("{{{{{}}}}}", True),
            ("((((((((((", False),
            ("))))))))))", False),
            ("(){}[]", True),
            ("([{}])", True),
            ("([{]})", False),
            ("(())", True),
            ("(()", False),
            ("())", False),
        ],
    )
    @logged_test
    def test_is_valid(self, s: str, expected: bool):
        result = self.solution.is_valid(s)
        assert result == expected
