class Solution:
    """
    Houses: [2, 7, 9, 3, 1]
    Can't rob adjacent houses!
    For each house: max(skip, rob) = max(prev1, prev2 + current)

    Step by step:
    i=0: prev2=0, prev1=0, num=2 → max(0, 0+2) = 2
    i=1: prev2=0, prev1=2, num=7 → max(2, 0+7) = 7
    i=2: prev2=2, prev1=7, num=9 → max(7, 2+9) = 11
    i=3: prev2=7, prev1=11, num=3 → max(11, 7+3) = 11
    i=4: prev2=11, prev1=11, num=1 → max(11, 11+1) = 12
    """

    # Time: O(n)
    # Space: O(1)
    def rob(self, nums: list[int]) -> int:
        prev2 = prev1 = 0  # prev2: max 2 ago, prev1: max 1 ago
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1
