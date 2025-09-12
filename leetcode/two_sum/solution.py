class Solution:

    # Time: O(n)
    # Space: O(n)
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
