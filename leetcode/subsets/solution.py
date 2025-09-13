class Solution:

    # Time: O(2^n)
    # Space: O(2^n)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start: int, path: list[int]) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
