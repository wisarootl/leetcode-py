from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        """
        Find the missing number using mathematical approach.

        The sum of numbers from 0 to n is n*(n+1)/2.
        The missing number is the difference between expected sum and actual sum.

        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


class SolutionOptimized:
    def missing_number(self, nums: List[int]) -> int:
        """
        Find the missing number using XOR approach.

        XOR has the property that a ^ a = 0 and a ^ 0 = a.
        If we XOR all numbers from 0 to n with all numbers in nums,
        the missing number will be the only one left.

        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        result = n  # Start with n since we're missing one number

        for i in range(n):
            result ^= i ^ nums[i]

        return result


class SolutionHashSet:
    def missing_number(self, nums: List[int]) -> int:
        """
        Find the missing number using hash set approach.

        Time: O(n)
        Space: O(n)
        """
        num_set = set(nums)
        n = len(nums)

        for i in range(n + 1):
            if i not in num_set:
                return i

        return -1  # Should never reach here


class SolutionSorting:
    def missing_number(self, nums: List[int]) -> int:
        """
        Find the missing number using sorting approach.

        Time: O(n log n)
        Space: O(1) if sorting in-place
        """
        nums.sort()
        n = len(nums)

        # Check if 0 is missing
        if nums[0] != 0:
            return 0

        # Check if n is missing
        if nums[-1] != n:
            return n

        # Check for missing number in between
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                return nums[i - 1] + 1

        return -1  # Should never reach here
