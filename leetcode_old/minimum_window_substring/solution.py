from collections import Counter


class Solution:
    # Sliding Window
    # Time: O(m + n) where m = len(s), n = len(t)
    # Space: O(k) where k is unique chars in t
    def min_window(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = Counter(t)

        left = 0
        formed = 0
        required = len(need)
        window_counts: dict[str, int] = {}

        # Result: (window length, left, right)
        ans: tuple[float, int | None, int | None] = (float("inf"), None, None)

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # Check if current char frequency matches desired frequency in t
            if char in need and window_counts[char] == need[char]:
                formed += 1

            # Contract window until it's no longer valid
            while left <= right and formed == required:
                char = s[left]

                # Update result if this window is smaller
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Remove from left
                window_counts[char] -= 1
                if char in need and window_counts[char] < need[char]:
                    formed -= 1

                left += 1

        if ans[0] == float("inf"):
            return ""
        assert ans[1] is not None and ans[2] is not None
        return s[ans[1] : ans[2] + 1]
