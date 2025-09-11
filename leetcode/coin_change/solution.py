class Solution:
    # Time: O(amount * len(coins))
    # Space: O(amount)
    def coin_change(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        # Initialize dp array with amount + 1 (impossible value)
        # Since max coins needed is amount (using all 1-cent coins)
        # amount + 1 serves as "infinity" to indicate impossible cases
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Return result: -1 if impossible, otherwise minimum coins needed
        return dp[amount] if dp[amount] <= amount else -1
