class Solution:

    # Time: O(1) - always 32 iterations
    # Space: O(1) - only using constant extra space
    def reverse_bits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.

        Algorithm:
        1. Initialize result to 0
        2. For each of the 32 bits:
           - Extract the rightmost bit of n using (n & 1)
           - Add it to the result at the appropriate position
           - Right shift n to get the next bit
           - Left shift result to make room for the next bit
        3. Return the result

        This approach is optimal for single calls. For multiple calls,
        we could use a lookup table for optimization.
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
