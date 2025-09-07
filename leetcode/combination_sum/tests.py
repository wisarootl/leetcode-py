import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestCombinationSum:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "candidates, target, expected",
        [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, []),
            ([1], 1, [[1]]),
            ([1], 2, [[1, 1]]),
            ([2, 3, 4], 6, [[2, 2, 2], [2, 4], [3, 3]]),
            (
                [7, 3, 2],
                18,
                [
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 3, 3],
                    [2, 2, 2, 3, 3, 3, 3],
                    [2, 2, 7, 7],
                    [2, 3, 3, 3, 7],
                    [3, 3, 3, 3, 3, 3],
                ],
            ),
        ],
    )
    @logged_test
    def test_combination_sum(self, candidates: list[int], target: int, expected: list[list[int]]):
        result = self.solution.combination_sum(candidates, target)
        # Sort both result and expected for comparison
        result_sorted = [sorted(combo) for combo in result]
        expected_sorted = [sorted(combo) for combo in expected]
        result_sorted.sort()
        expected_sorted.sort()
        assert result_sorted == expected_sorted
