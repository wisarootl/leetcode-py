class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_valid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in pairs:
                stack.append(char)
            elif not stack or pairs[stack.pop()] != char:
                return False

        return not stack
