import pytest

from leetcode_py import logged_test

from .helpers import assert_exist, run_exist
from .solution import Solution


class TestWordSearch:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "board, word, expected",
        [
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
            ([["A"]], "A", True),
            ([["A"]], "B", False),
            ([["A", "B"], ["C", "D"]], "ACDB", True),
            ([["A", "B"], ["C", "D"]], "ABDC", True),
            ([["A", "B"], ["C", "D"]], "ABCD", False),
            ([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS", False),
            (
                [
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                    ["A", "A", "A", "A", "A", "A"],
                ],
                "AAAAAAAAAAAAAAB",
                False,
            ),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SFCS", True),
        ],
    )
    def test_exist(self, board: list[list[str]], word: str, expected: bool):
        result = run_exist(Solution, board, word)
        assert_exist(result, expected)
