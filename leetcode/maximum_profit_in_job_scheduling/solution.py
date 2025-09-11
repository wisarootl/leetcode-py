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
