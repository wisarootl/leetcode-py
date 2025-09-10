import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestPermutations:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([], [[]]),
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1], [[1]]),
            ([-1, 0, 1], [[-1, 0, 1], [-1, 1, 0], [0, -1, 1], [0, 1, -1], [1, -1, 0], [1, 0, -1]]),
            ([4, 5], [[4, 5], [5, 4]]),
            ([1, 2, 3, 4], 24),  # Test count only for larger input
            ([10], [[10]]),
            ([-5, -3], [[-5, -3], [-3, -5]]),
        ],
    )
    @logged_test
    def test_permute(self, nums: list[int], expected):
        result = self.solution.permute(nums)

        # If expected is int, just check count (for larger inputs)
        if isinstance(expected, int):
            assert len(result) == expected
            # Verify all permutations are unique
            assert len(set(tuple(perm) for perm in result)) == expected
            return

        # Sort both result and expected for comparison since order doesn't matter
        result_sorted = [sorted(perm) for perm in result]
        expected_sorted = [sorted(perm) for perm in expected]
        result_sorted.sort()
        expected_sorted.sort()
        assert len(result) == len(expected)
        assert result_sorted == expected_sorted
