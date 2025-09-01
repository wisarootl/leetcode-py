import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestEvaluateReversePolishNotation:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["2", "1", "+", "3", "*"], 9),
            (["4", "13", "5", "/", "+"], 6),
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        ],
    )
    @logged_test
    def test_eval_rpn(self, tokens: list[str], expected: int):
        result = self.solution.eval_rpn(tokens)
        assert result == expected
