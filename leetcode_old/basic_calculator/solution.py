class Solution:
    # Time: O(n)
    # Space: O(n)
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        result = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                result += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                if len(stack) < 2:
                    raise ValueError("Mismatched parentheses")
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()
            elif char != " ":
                raise ValueError(f"Invalid character: '{char}'")

        if stack:
            raise ValueError("Mismatched parentheses")

        return result + sign * num


# Example walkthrough: "(1+(4+5+2)-3)+(6+8)" = 23
#
# char | num | sign | result | stack      | action
# -----|-----|------|--------|------------|------------------
# '('  | 0   | 1    | 0      | [0, 1]     | push result=0, sign=1
# '1'  | 1   | 1    | 0      | [0, 1]     | build num=1
# '+'  | 0   | 1    | 1      | [0, 1]     | result += 1*1 = 1
# '('  | 0   | 1    | 0      | [0,1,1,1]  | push result=1, sign=1
# '4'  | 4   | 1    | 0      | [0,1,1,1]  | build num=4
# '+'  | 0   | 1    | 4      | [0,1,1,1]  | result += 1*4 = 4
# '5'  | 5   | 1    | 4      | [0,1,1,1]  | build num=5
# '+'  | 0   | 1    | 9      | [0,1,1,1]  | result += 1*5 = 9
# '2'  | 2   | 1    | 9      | [0,1,1,1]  | build num=2
# ')'  | 0   | 1    | 11     | [0, 1]     | result=11*1+1 = 12
# '-'  | 0   | -1   | 12     | [0, 1]     | sign = -1
# '3'  | 3   | -1   | 12     | [0, 1]     | build num=3
# ')'  | 0   | 1    | 9      | []         | result=9*1+0 = 9
# '+'  | 0   | 1    | 9      | []         | sign = 1
# '('  | 0   | 1    | 0      | [9, 1]     | push result=9, sign=1
# '6'  | 6   | 1    | 0      | [9, 1]     | build num=6
# '+'  | 0   | 1    | 6      | [9, 1]     | result += 1*6 = 6
# '8'  | 8   | 1    | 6      | [9, 1]     | build num=8
# ')'  | 0   | 1    | 14     | []         | result=14*1+9 = 23
# end  | 0   | 1    | 14     | []         | return 14+1*0 = 23
