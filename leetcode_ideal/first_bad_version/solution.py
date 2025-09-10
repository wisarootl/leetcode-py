class Solution:
    # TODO: template constraint
    def __init__(self, first_bad):
        self.is_bad_version = lambda version: version >= first_bad

    # Time: O(log n)
    # Space: O(1)
    def first_bad_version(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if self.is_bad_version(mid):
                right = mid
            else:
                left = mid + 1

        return right


# BISECT PATTERNS - General Binary Search
# Given: arr = [10,20,30,30,30,40,50], target = 30
#               0  1  2  3  4  5  6
#
# bisect_left: Find FIRST occurrence (leftmost insertion point)
#   while left < right:
#       if arr[mid] >= target:  # >= keeps moving left
#           right = mid
#   Returns: 2 (index of first 30, value=30)
#            [10,20,30,30,30,40,50]
#             0  1  2  3  4  5  6
#                   ↑ index 2
#
# bisect_right: Find position AFTER last occurrence
#   while left < right:
#       if arr[mid] > target:   # > allows equal values
#           right = mid
#   Returns: 5 (index after last 30, value=40)
#            [10,20,30,30,30,40,50]
#             0  1  2  3  4  5  6
#                            ↑ index 5
#
# Key difference: >= vs > in the condition
# This problem uses bisect_left pattern to find first bad version
