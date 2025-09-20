class Solution:

    # Time: O(n log k) - each word processed with O(log k) heap operations
    # Space: O(n + k) - Counter takes O(n), heap takes O(k)
    def top_k_frequent(self, words: list[str], k: int) -> list[str]:
        import heapq
        from collections import Counter

        count = Counter(words)
        # Min-heap of size k: (freq, word)
        # Keep least frequent at top, reverse lexicographic for ties
        heap: list[tuple[int, str]] = []

        for word, freq in count.items():
            if len(heap) < k:
                # Min-heap: (freq, -word) for reverse lexicographic order
                heapq.heappush(heap, (freq, word))
            else:
                min_freq, min_word = heap[0]
                # Replace if current word has higher priority
                if freq > min_freq or (freq == min_freq and word < min_word):
                    heapq.heapreplace(heap, (freq, word))

        # Extract and sort results
        result = list(heap)
        result.sort(key=lambda x: (-x[0], x[1]))
        return [word for _, word in result]
