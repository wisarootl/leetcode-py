import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_eval_rpn, run_eval_rpn
from .solution import Solution


class TestEvaluateReversePolishNotation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["2", "1", "+", "3", "*"], 9),
            (["4", "13", "5", "/", "+"], 6),
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
            (["3"], 3),
            (["15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"], 5),
            (["2", "1", "+"], 3),
            (["2", "1", "-"], 1),
            (["3", "4", "*"], 12),
            (["8", "2", "/"], 4),
            (["5", "1", "2", "+", "4", "*", "+", "3", "-"], 14),
            (["-1", "2", "+"], 1),
            (["0", "3", "/"], 0),
            (["18", "6", "/", "3", "/"], 1),
        ],
    )
    def test_eval_rpn(self, tokens: list[str], expected: int):
        result = run_eval_rpn(Solution, tokens)
        assert_eval_rpn(result, expected)
