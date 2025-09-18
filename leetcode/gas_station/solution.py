class Solution:
    """
    Gas Station Circuit - Greedy Approach

    Visual Example: gas=[1,2,3,4,5], cost=[3,4,5,1,2]

         Station:  0   1   2   3   4
                  ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
         Gas:     │1│ │2│ │3│ │4│ │5│
                  └─┘ └─┘ └─┘ └─┘ └─┘
         Cost:     3   4   5   1   2
                   ↓   ↓   ↓   ↓   ↓
         Net:     -2  -2  -2  +3  +3

    Algorithm trace:
    i=0: tank=0+(-2)=-2 < 0 → reset tank=0, start=1
    i=1: tank=0+(-2)=-2 < 0 → reset tank=0, start=2
    i=2: tank=0+(-2)=-2 < 0 → reset tank=0, start=3
    i=3: tank=0+(+3)=+3 ≥ 0 → continue
    i=4: tank=3+(+3)=+6 ≥ 0 → return start=3

    Key insight: If total_gas ≥ total_cost, greedy start position works!
    """

    # Time: O(n)
    # Space: O(1)
    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start
