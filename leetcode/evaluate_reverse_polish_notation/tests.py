import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestEvaluateReversePolishNotation:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            # Original cases
            (["2", "1", "+", "3", "*"], 9),
            (["4", "13", "5", "/", "+"], 6),
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
            # Single number
            (["42"], 42),
            # Negative numbers
            (["-1"], -1),
            (["1", "-1", "+"], 0),
            # Basic operations
            (["3", "4", "+"], 7),
            (["5", "2", "-"], 3),
            (["6", "3", "*"], 18),
            (["8", "2", "/"], 4),
            # Division with negatives
            (["-3", "4", "+", "2", "*", "1", "-"], 1),
            # Complex expression
            (["15", "7", "1", "1", "+", "/", "/", "3", "*", "2", "1", "1", "+", "+", "-"], 11),
        ],
    )
    @logged_test
    def test_eval_rpn(self, tokens: list[str], expected: int):
        result = self.solution.eval_rpn(tokens)
        assert result == expected
