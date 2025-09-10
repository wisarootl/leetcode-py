import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_clone_graph, create_graph, run_clone_graph
from .solution import Solution, SolutionBFS, SolutionDFS


class TestCloneGraph:

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "adj_list",
        [
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[]],
            [],
        ],
    )
    def test_clone_graph(self, adj_list: list[list[int]], solution_class: type):
        result = run_clone_graph(solution_class, adj_list)
        expected = create_graph(adj_list)
        assert_clone_graph(result, expected)
