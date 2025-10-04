import heapq
from collections import Counter, defaultdict
from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find top k frequent elements using Counter and most_common.

        Time: O(n log n) - Counter.most_common() sorts internally
        Space: O(n) - for Counter and result
        """
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]


class SolutionOptimized:
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


class SolutionBucketSort:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket sort approach for O(n) time complexity.

        Time: O(n)
        Space: O(n)
        """
        counter = Counter(nums)
        n = len(nums)

        # Create buckets for each frequency
        buckets = defaultdict(list)
        for num, count in counter.items():
            buckets[count].append(num)

        # Collect top k elements from highest frequency buckets
        result = []
        for freq in range(n, 0, -1):
            if freq in buckets:
                result.extend(buckets[freq])
                if len(result) >= k:
                    break

        return result[:k]


class SolutionQuickSelect:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Quick select approach for O(n) average time complexity.

        Time: O(n) average, O(n^2) worst case
        Space: O(n)
        """
        counter = Counter(nums)
        unique_nums = list(counter.keys())

        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot_freq = counter[unique_nums[pivot_idx]]
            # Move pivot to end
            unique_nums[pivot_idx], unique_nums[right] = unique_nums[right], unique_nums[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if counter[unique_nums[i]] >= pivot_freq:
                    unique_nums[store_idx], unique_nums[i] = unique_nums[i], unique_nums[store_idx]
                    store_idx += 1

            # Move pivot to final position
            unique_nums[right], unique_nums[store_idx] = unique_nums[store_idx], unique_nums[right]
            return store_idx

        def quickselect(left: int, right: int, k: int) -> None:
            if left == right:
                return

            pivot_idx = left + (right - left) // 2
            pivot_idx = partition(left, right, pivot_idx)

            if k == pivot_idx:
                return
            elif k < pivot_idx:
                quickselect(left, pivot_idx - 1, k)
            else:
                quickselect(pivot_idx + 1, right, k)

        quickselect(0, len(unique_nums) - 1, k - 1)
        return unique_nums[:k]
