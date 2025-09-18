class Solution:

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
