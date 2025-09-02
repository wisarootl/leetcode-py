import pytest

from leetcode_py import GraphNode
from leetcode_py.test_utils import logged_test

from .solution import Solution, SolutionBFS, SolutionDFS


class TestCloneGraph:
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "adj_list",
        [[[2, 4], [1, 3], [2, 4], [1, 3]], [[]], []],
    )
    @logged_test
    def test_clone_graph(
        self,
        adj_list: list[list[int]],
        solution_class: type[Solution | SolutionDFS | SolutionBFS],
    ):
        solution = solution_class()
        node = GraphNode.from_adjacency_list(adj_list)
        result = solution.clone_graph(node)

        assert result.is_clone(node) if result else node is None
