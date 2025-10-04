from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Optimized version with better variable naming and edge case handling.

        Time: O(n)
        Space: O(1)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_range(start: int, end: int) -> int:
            """Rob houses from start to end (inclusive)."""
            prev_rob = prev_not_rob = 0
            for i in range(start, end + 1):
                current_rob = prev_not_rob + nums[i]
                current_not_rob = max(prev_rob, prev_not_rob)
                prev_rob, prev_not_rob = current_rob, current_not_rob
            return max(prev_rob, prev_not_rob)

        n = len(nums)
        # Case 1: Rob houses 0 to n-2 (exclude last house)
        case1 = rob_range(0, n - 2)

        # Case 2: Rob houses 1 to n-1 (exclude first house)
        case2 = rob_range(1, n - 1)

        return max(case1, case2)
