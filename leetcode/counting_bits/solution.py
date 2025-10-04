from typing import List


class Solution:
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
