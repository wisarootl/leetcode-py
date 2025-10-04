import heapq
from collections import Counter
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Optimized version using heap for O(n log k) time complexity.

        Time: O(n log k) - heap operations
        Space: O(n) - for counter and heap
        """
        counter = Counter(nums)

        # Use min heap of size k
        heap: list[tuple[int, int]] = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]
