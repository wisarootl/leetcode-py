class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_sub_array(self, nums: list[int]) -> int:
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
