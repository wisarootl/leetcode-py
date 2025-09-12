import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_right_side_view, run_right_side_view
from .solution import Solution, SolutionBFS, SolutionDFS


class TestBinaryTreeRightSideView:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionBFS, SolutionDFS])
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
        ],
    )
    def test_right_side_view(
        self, solution_class: type, root_list: list[int | None], expected: list[int]
    ):
        result = run_right_side_view(solution_class, root_list)
        assert_right_side_view(result, expected)
