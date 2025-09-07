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


# Example walkthrough: push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()
#
# Initial: stack=[], min_stack=[]
#
# push(-2): stack=[-2], min_stack=[-2]  (first element, add to both)
# push(0):  stack=[-2,0], min_stack=[-2]  (0 > -2, don't add to min_stack)
# push(-3): stack=[-2,0,-3], min_stack=[-2,-3]  (-3 <= -2, add to min_stack)
# getMin(): return -3  (top of min_stack)
# pop():    stack=[-2,0], min_stack=[-2]  (-3 was min, remove from both stacks)
# top():    return 0  (top of main stack)
# getMin(): return -2  (top of min_stack after pop)
