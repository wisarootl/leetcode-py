class Solution:

    # Time: O(n)
    # Space: O(1)
    # This follows Fibonacci pattern
    # Standard Fib: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5...
    def climb_stairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current

        return prev1
