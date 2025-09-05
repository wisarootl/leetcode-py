class Solution:
    # Time: O(n)
    # Space: O(1)
    def product_except_self(self, nums: list[int]) -> list[int]:
        # Example: nums = [1, 2, 3, 4]
        # Expected output: [24, 12, 8, 6]

        n = len(nums)
        result = [1] * n  # [1, 1, 1, 1]

        # Left pass: result[i] = product of all elements to the left of i
        # nums:   [1, 2, 3, 4]
        # result: [1, 1, 2, 6] (left products)
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Right pass: multiply by product of all elements to the right of i
        # right products: [24, 12, 4, 1]
        # result: [1*24, 1*12, 2*4, 6*1] = [24, 12, 8, 6]
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
