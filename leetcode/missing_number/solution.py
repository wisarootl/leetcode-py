class Solution:

    # Time: O(n)
    # Space: O(1)
    def missing_number(self, nums: list[int]) -> int:
        """
        Find the missing number in an array containing n distinct numbers
        in the range [0, n].

        Approach: Use the mathematical formula for sum of consecutive integers.
        The sum of numbers from 0 to n is n*(n+1)/2.
        The missing number = expected_sum - actual_sum.
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
