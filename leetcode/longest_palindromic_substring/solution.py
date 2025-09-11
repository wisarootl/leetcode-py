class Solution:

    # Time: O(n^2)
    # Space: O(1)
    def longest_palindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        for i in range(len(s)):
            # Odd length palindromes (center at i)
            len1 = self.expand(s, i, i)
            # Even length palindromes (center between i and i+1)
            len2 = self.expand(s, i, i + 1)

            curr_len = max(len1, len2)
            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2

        return s[start : start + max_len]

    @staticmethod
    def expand(s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


class SolutionManacher:
    # Time: O(n)
    # Space: O(n)
    def longest_palindrome(self, s: str) -> str:
        t = "#".join("^{}$".format(s))
        n = len(t)
        p = [0] * n
        center = right = 0
        for i in range(1, n - 1):
            mirror_value = 2 * center - i
            p[i] = min(right - i, p[mirror_value]) if right > i else 0

            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > right:
                center, right = i, i + p[i]

        max_len = max(p)
        center_index = p.index(max_len)

        # Map back to original string: (center_index - max_len) // 2
        start = (center_index - max_len) // 2
        return s[start : start + max_len]
