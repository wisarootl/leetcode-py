from collections import OrderedDict


class LRUCache:
    # Space: O(capacity)
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    # Time: O(1)
    # Space: O(1)
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move to end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    # Time: O(1)
    # Space: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add new
            if len(self.cache) >= self.capacity:
                # Remove LRU (first item)
                self.cache.popitem(last=False)

            self.cache[key] = value
