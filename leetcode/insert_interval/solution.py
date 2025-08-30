class Solution:
    # Time: O(n)
    # Space: O(n)
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0

        # Add intervals before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # Add remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
