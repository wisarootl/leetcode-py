class Solution:

    # Time: O(log(n-k))
    # Space: O(1)
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]:
        """
        Find k closest elements to x using binary search on window positions.

        Time: O(log(n-k)) - Binary search on n-k possible window positions
        Space: O(1) - Only using constant extra variables

        Algorithm:
        - Search space: all possible left boundaries for k-element window [0, n-k]
        - For each position mid, compare window boundaries: arr[mid] vs arr[mid+k]
        - If arr[mid] farther from x, move search right; otherwise move left
        - Leverages sorted array property for O(log) efficiency vs O(n) linear scan

        Example: arr=[0,1,2,3,4], k=3, x=3
        Windows: [0,1,2], [1,2,3], [2,3,4]
        Distances: max(2,1), max(0,1), max(1,1) → choose [1,2,3]
        """
        # Binary search to find the left boundary of the k-element window
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # Compare distances: arr[mid] vs arr[mid + k]
            # If arr[mid] is farther from x than arr[mid + k], move left boundary right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]
