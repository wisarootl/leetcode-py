import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_invert_tree, run_invert_tree


class TestInvertBinaryTree:
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
        ],
    )
    @logged_test
    def test_invert_tree_recursive(self, root_list: list[int | None], expected_list: list[int | None]):
        from .helpers import create_tree
        from .solution import Solution

        result = run_invert_tree(Solution, root_list)
        expected = create_tree(expected_list)
        assert_invert_tree(result, expected)

    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
        ],
    )
    @logged_test
    def test_invert_tree_dfs(self, root_list: list[int | None], expected_list: list[int | None]):
        from .helpers import create_tree
        from .solution import SolutionDFS

        result = run_invert_tree(SolutionDFS, root_list)
        expected = create_tree(expected_list)
        assert_invert_tree(result, expected)

    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
        ],
    )
    @logged_test
    def test_invert_tree_bfs(self, root_list: list[int | None], expected_list: list[int | None]):
        from .helpers import create_tree
        from .solution import SolutionBFS

        result = run_invert_tree(SolutionBFS, root_list)
        expected = create_tree(expected_list)
        assert_invert_tree(result, expected)
