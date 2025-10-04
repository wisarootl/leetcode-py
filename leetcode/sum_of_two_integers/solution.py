class Solution:

    # Time: O(1) - constant time bit operations
    # Space: O(1) - no extra space used
    def get_sum(self, a: int, b: int) -> int:
        """
        Add two integers without using + or - operators.
        Uses bit manipulation approach:
        1. XOR gives us the sum without carry
        2. AND + left shift gives us the carry
        3. Repeat until no carry remains
        """
        # Handle 32-bit signed integer overflow
        mask = 0xFFFFFFFF

        while b != 0:
            # Calculate sum without carry
            sum_without_carry = (a ^ b) & mask
            # Calculate carry
            carry = ((a & b) << 1) & mask
            a = sum_without_carry
            b = carry

        # Handle negative result for 32-bit signed integer
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a
