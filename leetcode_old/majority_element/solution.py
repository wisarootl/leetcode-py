class Solution:
    # Time: O(n)
    # Space: O(1)
    def majority_element(self, nums: list[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
