class MyQueue:
    # Time: O(1)
    # Space: O(n)
    def __init__(self) -> None:
        self.input_stack: list[int] = []
        self.output_stack: list[int] = []

    # Time: O(1)
    # Space: O(1)
    def push(self, x: int) -> None:
        self.input_stack.append(x)

    # Time: O(1) amortized
    # Space: O(1)
    def pop(self) -> int:
        self._move_to_output()
        return self.output_stack.pop()

    # Time: O(1) amortized
    # Space: O(1)
    def peek(self) -> int:
        self._move_to_output()
        return self.output_stack[-1]

    # Time: O(1)
    # Space: O(1)
    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack

    def _move_to_output(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


# Amortized O(1) Explanation:
# Example with 4 push + 4 pop operations:
#
# push(1)  # input: [1], output: []           - O(1)
# push(2)  # input: [1,2], output: []         - O(1)
# push(3)  # input: [1,2,3], output: []       - O(1)
# push(4)  # input: [1,2,3,4], output: []     - O(1)
#
# pop()    # Move all 4 to output: input: [], output: [4,3,2,1] then pop 1  - O(4)
# pop()    # output: [4,3,2], just pop 2                                     - O(1)
# pop()    # output: [4,3], just pop 3                                       - O(1)
# pop()    # output: [4], just pop 4                                         - O(1)
#
# Total cost: 4 + 4 + 1 + 1 + 1 = 11 operations for 8 calls = 1.4 per operation
# Key: Each element moves exactly once from input to output, so expensive O(n)
# transfer is "spread out" over multiple cheap O(1) operations = amortized O(1)
