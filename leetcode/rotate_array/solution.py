class Solution:

    # Time: O(n) - three passes through array
    # Space: O(1) - in-place rotation using reversal
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate array right by k steps using triple reversal.

        Example: nums = [1,2,3,4,5,6,7], k = 3

        Step 1: Reverse entire array
        [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]

        Step 2: Reverse first k elements
        [7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]
                ↑k=3↑

        Step 3: Reverse remaining elements
        [5,6,7,4,3,2,1] → [5,6,7,1,2,3,4] ✓
              ↑remaining↑
        """
        n = len(nums)
        k = k % n  # Handle k > n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse entire array
        reverse(0, n - 1)
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        # Step 3: Reverse remaining elements
        reverse(k, n - 1)
