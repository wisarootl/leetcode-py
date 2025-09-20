class Solution:

    # Time: O(n)
    # Space: O(1)
    def find_duplicate(self, nums: list[int]) -> int:
        """
        Floyd's cycle detection - treat array as implicit linked list.

        Example: nums = [1, 3, 4, 2, 2]

        Array as linked list:
        Index:  0  1  2  3  4
        Value: [1, 3, 4, 2, 2]
                ↓  ↓  ↓  ↓  ↓
        Points: 1  3  4  2  2

        Following pointers: 0→1→3→2→4→2→4→2... (cycle!)

        Visual cycle:
            0
            ↓
            1 ← start
            ↓
            3
            ↓
            2 ←─┐ (duplicate = cycle entrance)
            ↓   │
            4 ──┘

        Phase 1: Find intersection using slow/fast pointers
        Phase 2: Find cycle entrance (duplicate) by resetting slow to start

        The duplicate creates the cycle entrance because multiple indices point to it.
        """
        slow = fast = nums[0]

        # Find intersection point in cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find entrance to cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
