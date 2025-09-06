class Solution:
    # Time: O(n)
    # Space: O(n)
    def contains_duplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
