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

        # Use min heap of size k - keep the k most frequent elements
        heap: list[tuple[int, int]] = []
        for num, count in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))

        # Extract numbers from heap (order doesn't matter for this problem)
        return [num for _, num in heap]
