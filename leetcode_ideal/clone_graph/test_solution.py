import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_clone_graph, create_graph, run_clone_graph


class TestCloneGraph:
    @pytest.mark.parametrize(
        "adj_list",
        [
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[]],
            [],
        ],
    )
    @logged_test
    def test_clone_graph_recursive(self, adj_list: list[list[int]]):
        from .solution import Solution

        result = run_clone_graph(Solution, adj_list)
        expected = create_graph(adj_list)
        assert_clone_graph(result, expected)

    @pytest.mark.parametrize(
        "adj_list",
        [
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[]],
            [],
        ],
    )
    @logged_test
    def test_clone_graph_dfs(self, adj_list: list[list[int]]):
        from .solution import SolutionDFS

        result = run_clone_graph(SolutionDFS, adj_list)
        expected = create_graph(adj_list)
        assert_clone_graph(result, expected)

    @pytest.mark.parametrize(
        "adj_list",
        [
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[]],
            [],
        ],
    )
    @logged_test
    def test_clone_graph_bfs(self, adj_list: list[list[int]]):
        from .solution import SolutionBFS

        result = run_clone_graph(SolutionBFS, adj_list)
        expected = create_graph(adj_list)
        assert_clone_graph(result, expected)
