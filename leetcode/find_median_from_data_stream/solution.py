import heapq


class MedianFinder:
    # Two balanced heaps approach for general streaming median
    # Time: O(1) init
    # Space: O(n)
    def __init__(self) -> None:
        self.small: list[int] = []  # max heap (negated)
        self.large: list[int] = []  # min heap

    # Time: O(log n)
    # Space: O(1)
    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    # Time: O(1)
    # Space: O(1)
    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0


class MedianFinderHybrid:
    # Hybrid counting array + heaps for bounded ranges with outliers
    # Time: O(1) init
    # Space: O(R + k) where R = range_size, k = outliers
    def __init__(self, min_val: int = 0, max_val: int = 100) -> None:
        self.min_val = min_val
        self.max_val = max_val
        self.counts = [0] * (max_val - min_val + 1)
        self.outliers_small: list[int] = []  # max heap for < min_val
        self.outliers_large: list[int] = []  # min heap for > max_val
        self.total = 0

    # Time: O(1) for range, O(log k) for outliers
    # Space: O(1)
    def add_num(self, num: int) -> None:
        if self.min_val <= num <= self.max_val:
            self.counts[num - self.min_val] += 1
        elif num < self.min_val:
            heapq.heappush(self.outliers_small, -num)
        else:
            heapq.heappush(self.outliers_large, num)
        self.total += 1

    # Time: O(R + k log k) worst case, O(R) typical, O(1) if R constant
    # Space: O(k) for sorting outliers
    def find_median(self) -> float:
        target = self.total // 2
        count = 0

        # Count outliers < 0
        outliers_small_count = len(self.outliers_small)
        if count + outliers_small_count > target:
            sorted_small = sorted([-x for x in self.outliers_small])
            if self.total % 2 == 1:
                return sorted_small[target - count]
            else:
                if target - count == 0:
                    return (sorted_small[0] + self._get_next_value(0)) / 2.0
                return (sorted_small[target - count - 1] + sorted_small[target - count]) / 2.0
        count += outliers_small_count

        # Count [min_val, max_val] range
        for i in range(len(self.counts)):
            if count + self.counts[i] > target:
                val = i + self.min_val
                if self.total % 2 == 1:
                    return val
                else:
                    if target == count:
                        return (self._get_prev_value(count - 1) + val) / 2.0
                    return val
            count += self.counts[i]

        # Must be in outliers > 100
        sorted_large = sorted(self.outliers_large)
        idx = target - count
        if self.total % 2 == 1:
            return sorted_large[idx]
        else:
            if idx == 0:
                return (self._get_prev_value(count - 1) + sorted_large[0]) / 2.0
            return (sorted_large[idx - 1] + sorted_large[idx]) / 2.0

    def _get_prev_value(self, pos: int) -> int:
        count = 0
        # Check outliers < 0
        if pos < len(self.outliers_small):
            return sorted([-x for x in self.outliers_small])[pos]
        count += len(self.outliers_small)

        # Check [min_val, max_val] range
        for i in range(len(self.counts)):
            if count + self.counts[i] > pos:
                return i + self.min_val
            count += self.counts[i]

        # Must be in outliers > 100
        return sorted(self.outliers_large)[pos - count]

    def _get_next_value(self, pos: int) -> int:
        return self._get_prev_value(pos + 1)
