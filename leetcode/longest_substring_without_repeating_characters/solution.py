class Solution:
    # Time: O(n)
    # Space: O(min(m, n)) where m is charset size
    def length_of_longest_substring(self, s: str) -> int:
        seen: set[str] = set()
        left = max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
