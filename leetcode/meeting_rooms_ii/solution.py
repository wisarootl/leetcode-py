class Solution:

    # Time: O(n log n)
    # Space: O(n)
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Separate start and end times
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        rooms = 0
        max_rooms = 0
        start_ptr = end_ptr = 0

        # Two pointer approach
        while start_ptr < len(intervals):
            if starts[start_ptr] < ends[end_ptr]:
                # Meeting starts, need a room
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_ptr += 1
            else:
                # Meeting ends, free a room
                rooms -= 1
                end_ptr += 1

        return max_rooms
