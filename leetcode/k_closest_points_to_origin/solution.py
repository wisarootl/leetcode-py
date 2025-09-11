import heapq


class Solution:
    # Time: O(n log k)
    # Space: O(k)
    def k_closest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap: list[tuple[int, list[int]]] = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]
