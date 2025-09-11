class Solution:

    # Time: O(n * sum)
    # Space: O(sum)
    def can_partition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

            # Early termination: found target sum!
            if dp[target]:
                return True

        return False
