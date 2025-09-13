class Solution:
    # Dynamic Programming
    # Time: O(m * n)
    # Space: O(min(m, n))
    def unique_paths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m
        dp = [1] * m
        for _ in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j - 1]
        return dp[m - 1]


class SolutionMath:

    # Math solution: C(m+n-2, m-1) = (m+n-2)! / ((m-1)! * (n-1)!)
    # Time: O(min(m, n))
    # Space: O(1)
    def unique_paths(self, m: int, n: int) -> int:
        # Total moves: (m-1) right + (n-1) down = m+n-2
        # Choose (m-1) positions for right moves out of (m+n-2) total
        if m > n:
            m, n = n, m  # Optimize for smaller factorial

        result = 1
        for i in range(m - 1):
            result = result * (n + i) // (i + 1)
        return result
