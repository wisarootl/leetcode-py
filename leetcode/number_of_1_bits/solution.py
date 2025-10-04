class Solution:

    # Time: O(1) - at most 32 iterations (number of bits in int)
    # Space: O(1) - only using constant extra space
    def hammingWeight(self, n: int) -> int:
        """
        Count the number of set bits (1s) in the binary representation of n.

        Uses the Brian Kernighan's algorithm:
        n & (n-1) removes the rightmost set bit from n.
        We keep doing this until n becomes 0, counting each iteration.

        This is more efficient than checking each bit individually
        because it only iterates for the number of set bits, not all bits.
        """
        count = 0
        while n:
            count += 1
            n &= n - 1  # Remove the rightmost set bit
        return count
