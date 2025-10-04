class Solution:

    # Time: O(n^2) - expand around centers approach
    # Space: O(1) - no extra space used
    def countSubstrings(self, s: str) -> int:
        """
        Count palindromic substrings using expand around centers approach.
        For each possible center (single char or between two chars), expand outward
        and count palindromes.
        """
        if not s:
            return 0

        count = 0
        n = len(s)

        for i in range(n):
            # Odd length palindromes (center at i)
            count += self._expand_around_center(s, i, i)

            # Even length palindromes (center between i and i+1)
            count += self._expand_around_center(s, i, i + 1)

        return count

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        """Expand around center and count palindromes."""
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
