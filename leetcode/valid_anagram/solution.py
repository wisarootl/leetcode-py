from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1) - at most 26 unique characters
    def is_anagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
