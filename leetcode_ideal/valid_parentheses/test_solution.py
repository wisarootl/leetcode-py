import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_is_valid, run_is_valid


class TestValidParentheses:
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
        from .solution import Solution

        result = run_is_valid(Solution, s)
        assert_is_valid(result, expected)
