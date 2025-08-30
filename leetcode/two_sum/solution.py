from typing import List


class Solution:
    # Time: O(n) - single pass through array
    # Space: O(n) - hash map stores up to n elements
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]
            seen[num] = i
        return []
