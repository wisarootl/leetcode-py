class Solution:

    # Time: O(log(min(m, n)))
    # Space: O(1)
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition_x = (left + right) // 2
            partition_y = (m + n + 1) // 2 - partition_x

            # Handle edge cases
            max_left_x = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float("inf") if partition_x == m else nums1[partition_x]

            max_left_y = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float("inf") if partition_y == n else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return float(max(max_left_x, max_left_y))
            elif max_left_x > min_right_y:
                # Too far right in nums1
                right = partition_x - 1
            else:
                # Too far left in nums1
                left = partition_x + 1

        return 0.0
