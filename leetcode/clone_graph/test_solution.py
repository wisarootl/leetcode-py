import pytest

from leetcode_py import logged_test

from .helpers import assert_clone_graph, run_clone_graph
from .solution import Solution, SolutionBFS, SolutionDFS


class TestCloneGraph:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionBFS, SolutionDFS])
    @pytest.mark.parametrize(
        "adj_list",
        [
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[]],
            [],
            [[2], [1]],
            [[2, 3], [1], [1]],
            [[2], [3], [4], []],
            [[2, 3, 4], [1], [1], [1]],
            [[2, 3], [1, 3], [1, 2]],
            [[2, 5], [1, 3], [2, 4], [3, 5], [1, 4]],
            [[2, 3], [1, 4], [1, 4], [2, 3]],
            [[2, 3, 4, 5], [1], [1], [1], [1]],
            [[2], [3], [4], [5], []],
        ],
    )
    def test_clone_graph(self, solution_class: type, adj_list: list[list[int]]):
        result = run_clone_graph(solution_class, adj_list)
        assert_clone_graph(result, adj_list)
