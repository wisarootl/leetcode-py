import bisect


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def job_scheduling(self, start_time: list[int], end_time: list[int], profit: list[int]) -> int:

        jobs = sorted(zip(end_time, start_time, profit))
        dp = [0] * len(jobs)

        for i, (end, start, p) in enumerate(jobs):
            # Binary search for latest non-overlapping job
            j = bisect.bisect_right([job[0] for job in jobs[:i]], start) - 1

            # Take current job + best profit from non-overlapping jobs
            take = p + (dp[j] if j >= 0 else 0)
            # Skip current job
            skip = dp[i - 1] if i > 0 else 0

            dp[i] = max(take, skip)

        return dp[-1] if jobs else 0


# bisect and insort Explanation:
#
# Etymology: "bisect" = bi (two) + sect (cut) = cut into two parts
# Bisection method = binary search algorithm that repeatedly cuts search space in half
#
# bisect module provides binary search for SORTED lists (O(log n)):
# - bisect_left(arr, x): leftmost insertion position
# - bisect_right(arr, x): rightmost insertion position (default)
# - bisect(arr, x): alias for bisect_right
#
# insort module maintains sorted order while inserting:
# - insort_left(arr, x): insert at leftmost position
# - insort_right(arr, x): insert at rightmost position (default)
# - insort(arr, x): alias for insort_right
#
# Examples:
# arr = [1, 3, 3, 5]
# bisect_left(arr, 3) → 1   (before existing 3s)
# bisect_right(arr, 3) → 3  (after existing 3s)
# bisect_right(arr, 4) → 3  (between 3 and 5)
#
# insort(arr, 4) → arr becomes [1, 3, 3, 4, 5]
#
# In our solution:
# bisect_right([2,4,6], 5) = 2 (insertion position)
# j = 2 - 1 = 1 (index of latest job ending ≤ start_time)
