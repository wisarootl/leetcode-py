class Solution:
    # Time: O(len(a) + len(b))
    # Space: O(len(a) + len(b))
    def add_binary(self, a: str, b: str) -> str:
        # int(a, 2) converts binary string to decimal: int("11", 2) → 3
        # bin() converts decimal to binary string with prefix: bin(3) → '0b11'
        # [2:] removes the '0b' prefix to get just binary digits
        return bin(int(a, 2) + int(b, 2))[2:]


# Python Base Conversion:
#
# String → Integer (using int() with base parameter):
# - int("1010", 2) → 10 (binary to decimal)
# - int("ff", 16) → 255 (hex to decimal)
# - int("10", 8) → 8 (octal to decimal)
#
# Integer → String (conversion functions add prefixes):
# - bin(10) → '0b1010' (binary with '0b' prefix)
# - hex(255) → '0xff' (hex with '0x' prefix)
# - oct(8) → '0o10' (octal with '0o' prefix)
#
# These prefixes match Python literal syntax:
# - 0b1010 = 10, 0xff = 255, 0o10 = 8
#
# For string problems, slice off the prefix: bin(n)[2:] gives just the digits.
