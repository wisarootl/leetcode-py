class Solution:

    # Time: O(n) - single pass through string
    # Space: O(1) - at most 26 characters in count dict
    def character_replacement(self, s: str, k: int) -> int:
        """
        Find the length of the longest substring with same character
        after at most k replacements using sliding window approach.
        """
        if not s:
            return 0

        count: dict[str, int] = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            # Expand window: add character at right pointer
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # Shrink window if needed: if we need more than k replacements
            # Current window size = right - left + 1
            # Characters to replace = window_size - max_freq
            # If characters_to_replace > k, we need to shrink
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update max length
            max_length = max(max_length, right - left + 1)

        return max_length
