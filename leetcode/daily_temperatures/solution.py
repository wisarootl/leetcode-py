class Solution:

    # Time: O(n)
    # Space: O(n)
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack: list[int] = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
