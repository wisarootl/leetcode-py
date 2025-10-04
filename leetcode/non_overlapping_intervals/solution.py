class Solution:

    # Time: O(n log n) - sorting dominates
    # Space: O(1) - no extra space used
    def erase_overlap_intervals(self, intervals: list[list[int]]) -> int:
        """
        Find minimum number of intervals to remove to make non-overlapping.
        Uses greedy approach: sort by end time and keep intervals with earliest end times.
        """
        if not intervals:
            return 0

        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            # If current interval starts before previous ends, it overlaps
            if intervals[i][0] < prev_end:
                count += 1  # Remove this interval
            else:
                # No overlap, update previous end time
                prev_end = intervals[i][1]

        return count
