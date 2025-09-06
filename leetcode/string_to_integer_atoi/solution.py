class Solution:
    # Time: O(n)
    # Space: O(1)
    def my_atoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip whitespace
        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        # Check sign
        sign = 1
        if s[i] in {"+", "-"}:
            sign = -1 if s[i] == "-" else 1
            i += 1

        # Convert digits
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Clamp to 32-bit range
        return max(-(2**31), min(2**31 - 1, result))
