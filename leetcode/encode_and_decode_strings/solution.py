class Solution:

    # Time: O(n)
    # Space: O(n)
    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for s in strs:
            # Format: length + '#' + string
            encoded += str(len(s)) + "#" + s
        return encoded

    # Time: O(n)
    # Space: O(n)
    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1

            # Extract length
            length = int(s[i:j])

            # Extract string of that length
            decoded.append(s[j + 1 : j + 1 + length])

            # Move to next encoded string
            i = j + 1 + length

        return decoded
