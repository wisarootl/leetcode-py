class MinStack:
    # Time: O(1) for all operations
    # Space: O(n) where n is number of elements
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    # Time: O(1)
    # Space: O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    # Time: O(1)
    # Space: O(1)
    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    # Time: O(1)
    # Space: O(1)
    def top(self) -> int:
        return self.stack[-1]

    # Time: O(1)
    # Space: O(1)
    def get_min(self) -> int:
        return self.min_stack[-1]
