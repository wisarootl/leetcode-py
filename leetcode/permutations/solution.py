class Solution:
    # Time: O(n! * n)
    # Space: O(n! * n) output + O(n) recursion
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start: int) -> None:
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result
