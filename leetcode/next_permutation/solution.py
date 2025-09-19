class Solution:

    # Time: O(n)
    # Space: O(1)
    def next_permutation(self, nums: list[int]) -> None:
        # Find pivot (rightmost ascending pair)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find successor (rightmost element > pivot)
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse suffix
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
