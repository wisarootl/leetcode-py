import pytest

from leetcode_py import logged_test

from .helpers import assert_right_side_view, run_right_side_view
from .solution import Solution, SolutionBFS, SolutionDFS


class TestBinaryTreeRightSideView:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
            ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
            ([1, None, 3], [1, 3]),
            ([], []),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, 3], [1, 3]),
            ([1, 2, None, 4], [1, 2, 4]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 7]),
            ([1, 2, 3, None, None, 4, 5], [1, 3, 5]),
            ([5, 4, 6, None, None, None, 7], [5, 6, 7]),
            ([1, 2, 3, 4, 5, None, None, 8], [1, 3, 5, 8]),
            ([10, 5, 15, None, 6, 12, 20], [10, 15, 20]),
        ],
    )
    def test_right_side_view(
        self, solution_class: type, root_list: list[int | None], expected: list[int]
    ):
        result = run_right_side_view(solution_class, root_list)
        assert_right_side_view(result, expected)
