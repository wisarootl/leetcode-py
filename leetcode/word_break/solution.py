class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def word_break(self, s: str, word_dict: list[str]) -> bool:
        word_set = set(word_dict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]
