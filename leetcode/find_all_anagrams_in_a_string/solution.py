from collections import Counter


class Solution:
    """
    Sliding Window with Character Frequency Counting

    Algorithm:
    1. Count character frequencies in pattern p
    2. Use sliding window of size len(p) on string s
    3. Maintain frequency count of current window
    4. When frequencies match, record start index

    ASCII Visualization:
    s = "cbaebabacd", p = "abc" (need: a=1, b=1, c=1)

    Window positions:
    [cba]ebabacd  -> {c:1, b:1, a:1} ✓ matches -> index 0
    c[bae]babacd  -> {b:1, a:1, e:1} ✗
    cb[aeb]abacd  -> {a:1, e:1, b:1} ✗
    cba[eba]bacd  -> {e:1, b:1, a:1} ✗
    cbae[bab]acd  -> {b:2, a:1} ✗
    cbaeb[aba]cd  -> {a:2, b:1} ✗
    cbaeba[bac]d  -> {b:1, a:1, c:1} ✓ matches -> index 6
    """

    # Time: O(n) where n is length of s
    # Space: O(1) - at most 26 lowercase letters
    def find_anagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        result = []
        p_count = Counter(p)
        window_count = Counter(s[: len(p)])

        # Check first window
        if window_count == p_count:
            result.append(0)

        # Slide window
        for i in range(len(p), len(s)):
            # Add new character
            window_count[s[i]] += 1

            # Remove old character
            left_char = s[i - len(p)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Check if current window is anagram
            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result
