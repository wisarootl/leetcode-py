class Solution:
    # Time: O(n)
    # Space: O(n)
    def eval_rpn(self, tokens: list[str]) -> int:
        stack: list[int] = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]
