class TimeMap:
    # Time: O(1)
    # Space: O(n)
    def __init__(self) -> None:
        self.store: dict[str, list[tuple[int, str]]] = {}

    # Time: O(1)
    # Space: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    # Time: O(log n)
    # Space: O(1)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result
