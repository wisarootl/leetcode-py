import heapq
from collections import Counter, deque


class Solution:
    # Time: O(T * n + m log m) where T = len(tasks), worst case with many idle periods
    # Space: O(m) where m ≤ 26, so O(1)
    def least_interval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        step_num = 0
        queue: deque[tuple[int, int]] = deque()  # (count, available_time)

        while max_heap or queue:
            step_num += 1

            while queue and queue[0][1] <= step_num:
                count, _ = queue.popleft()
                heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # Decrease count (was negative)
                if count < 0:  # Still has tasks left
                    queue.append((count, step_num + n + 1))

        return step_num


class SolutionGreedy:
    # Time: O(T + m) where T = len(tasks), m = unique tasks ≤ 26, so O(T)
    # Space: O(m) where m ≤ 26, so O(1)
    def least_interval(self, tasks: list[str], n: int) -> int:
        """
        Mathematical approach:

        Key insight: The most frequent task determines the minimum time.

        Example: tasks=["A","A","A","B","B","B"], n=2

        1. Find max frequency: max_freq = 3 (A and B both appear 3 times)
        2. Count tasks with max frequency: max_count = 2 (A and B)
        3. Create frame structure:
           Frame: A B _ | A B _ | A B
           - (max_freq - 1) complete frames of size (n + 1)
           - Last frame contains only max frequency tasks

        4. Calculate minimum intervals:
           - Frame intervals: (max_freq - 1) * (n + 1) = 2 * 3 = 6
           - Plus max frequency tasks: 6 + 2 = 8

        5. Return max(total_tasks, calculated_min) to handle cases where
           we have enough variety to fill all gaps without idle time.
        """
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for freq in counts.values() if freq == max_freq)

        # Minimum intervals needed based on most frequent tasks
        min_intervals = (max_freq - 1) * (n + 1) + max_count

        # Return max to handle cases with sufficient task variety
        return max(len(tasks), min_intervals)
