class Solution:

    # Time: O(n) - single pass through string
    # Space: O(n) - stack storage for nested brackets
    def decode_string(self, s: str) -> str:
        """
        Decode string using stack for nested brackets.

        Example: s = "2[b3[a]]" → "baaabaaa"

        Process: 2 [ b 3 [ a ] ]

        char='2': num=2
        char='[': push('', 2), reset
        char='b': str='b'
        char='3': num=3
        char='[': push('b', 3), reset
        char='a': str='a'
        char=']': pop('b', 3) → str = 'b' + 'a'*3 = 'baaa'
        char=']': pop('', 2) → str = '' + 'baaa'*2 = 'baaabaaa'
        """
        stack = []
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                # Push current state and reset
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == "]":
                # Pop and construct
                prev_str, repeat_count = stack.pop()
                current_str = prev_str + current_str * repeat_count
            else:
                current_str += char

        return current_str
