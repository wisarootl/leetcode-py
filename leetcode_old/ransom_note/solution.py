from collections import Counter


class Solution:
    # Time: O(m + n) where m = magazine length, n = ransom_note length
    # Space: O(1) - at most 26 lowercase letters
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        if len(ransom_note) > len(magazine):
            return False

        magazine_count = Counter(magazine)

        for char in ransom_note:
            if magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1

        return True
