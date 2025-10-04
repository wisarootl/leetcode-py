class Solution:

    # Time: O(log n) - binary search
    # Space: O(1) - only using constant extra space
    def find_min(self, nums: list[int]) -> int:
        """
        Find the minimum element in a rotated sorted array using binary search.

        The key insight is that in a rotated sorted array, one half is always sorted.
        We can determine which half contains the minimum by comparing the middle
        element with the rightmost element.

        Algorithm:
        1. If nums[left] < nums[right], the array is not rotated, return nums[left]
        2. Otherwise, find the rotation point using binary search
        3. The minimum is always at the rotation point
        """
        left, right = 0, len(nums) - 1

        # If the array is not rotated, the first element is the minimum
        if nums[left] < nums[right]:
            return nums[left]

        # Binary search to find the rotation point
        while left < right:
            mid = left + (right - left) // 2

            # If mid element is greater than right element,
            # the rotation point is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If mid element is less than or equal to right element,
                # the rotation point is in the left half (including mid)
                right = mid

        return nums[left]
