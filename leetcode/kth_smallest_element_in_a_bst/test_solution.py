import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_kth_smallest, run_kth_smallest
from .solution import Solution


class TestKthSmallestElementInABst:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, k, expected",
        [
            ([3, 1, 4, None, 2], 1, 1),
            ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
            ([1], 1, 1),
            ([2, 1, 3], 2, 2),
            ([4, 2, 6, 1, 3, 5, 7], 4, 4),
            ([1, None, 2], 2, 2),
            ([5, 3, 6, 2, 4, None, None, 1], 1, 1),
            ([5, 3, 6, 2, 4, None, None, 1], 4, 4),
            ([10, 5, 15, 3, 7, 12, 20], 1, 3),
            ([10, 5, 15, 3, 7, 12, 20], 7, 20),
            ([1, None, 2, None, 3], 3, 3),
            ([3, 1, 4, None, 2], 4, 4),
        ],
    )
    def test_kth_smallest(self, root_list: list[int | None], k: int, expected: int):
        result = run_kth_smallest(Solution, root_list, k)
        assert_kth_smallest(result, expected)
