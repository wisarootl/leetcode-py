import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_k_group, run_reverse_k_group
from .solution import Solution


class TestReverseNodesInKGroup:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, k, expected_vals",
        [
            ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
            ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),
            ([1], 1, [1]),
            ([1, 2], 1, [1, 2]),
            ([1, 2], 2, [2, 1]),
            ([1, 2, 3], 1, [1, 2, 3]),
            ([1, 2, 3], 2, [2, 1, 3]),
            ([1, 2, 3], 3, [3, 2, 1]),
            ([1, 2, 3, 4], 2, [2, 1, 4, 3]),
            ([1, 2, 3, 4], 3, [3, 2, 1, 4]),
            ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
            ([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5]),
            ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
            ([1, 2, 3, 4, 5, 6], 4, [4, 3, 2, 1, 5, 6]),
            ([1, 2, 3, 4, 5, 6, 7], 2, [2, 1, 4, 3, 6, 5, 7]),
            ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7]),
            ([1, 2, 3, 4, 5, 6, 7, 8], 2, [2, 1, 4, 3, 6, 5, 8, 7]),
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, [3, 2, 1, 6, 5, 4, 7, 8]),
        ],
    )
    def test_reverse_k_group(self, head_vals: list[int], k: int, expected_vals: list[int]):
        result = run_reverse_k_group(Solution, head_vals, k)
        assert_reverse_k_group(result, expected_vals)
