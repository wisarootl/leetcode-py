class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_area(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area_so_far = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area_so_far = max(area, max_area_so_far)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max_area_so_far
