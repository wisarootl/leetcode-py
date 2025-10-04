from typing import List


class Solution:
    def count_bits(self, n: int) -> List[int]:
        """
        Count bits using dynamic programming approach.

        Key insight: For any number i, the number of 1s in its binary representation
        is equal to the number of 1s in i >> 1 (right shift by 1) plus the least significant bit.

        Time: O(n)
        Space: O(1) excluding output array
        """
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            # result[i] = result[i >> 1] + (i & 1)
            # i >> 1 removes the least significant bit
            # i & 1 gets the least significant bit
            result[i] = result[i >> 1] + (i & 1)

        return result


class SolutionOptimized:
    def count_bits(self, n: int) -> List[int]:
        """
        Optimized version with better variable naming and comments.

        Time: O(n)
        Space: O(1) excluding output array
        """
        if n == 0:
            return [0]

        bits_count = [0] * (n + 1)

        for num in range(1, n + 1):
            # For any number, the count of 1s equals:
            # count of 1s in (num >> 1) + whether the last bit is 1
            bits_count[num] = bits_count[num >> 1] + (num & 1)

        return bits_count


class SolutionNaive:
    def count_bits(self, n: int) -> List[int]:
        """
        Naive approach using built-in bin() function.

        Time: O(n log n) - bin() takes O(log n) time
        Space: O(1) excluding output array
        """
        result = []
        for i in range(n + 1):
            result.append(bin(i).count("1"))
        return result


class SolutionBitManipulation:
    def count_bits(self, n: int) -> List[int]:
        """
        Using bit manipulation to count 1s directly.

        Time: O(n log n) - each number takes O(log n) time
        Space: O(1) excluding output array
        """
        result = []

        for i in range(n + 1):
            count = 0
            num = i
            while num > 0:
                count += num & 1  # Check if least significant bit is 1
                num >>= 1  # Right shift to check next bit
            result.append(count)

        return result
