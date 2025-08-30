class Solution:
    # Time: O(n)
    # Space: O(n)
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        result = []
        i = 0

        # Add intervals before new_interval
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        result.append(new_interval)

        # Add remaining intervals
        result.extend(intervals[i:])
        return result
