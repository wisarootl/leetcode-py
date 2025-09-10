class Solution:
    # Dutch National Flag Algorithm - partitions array into 3 regions using 2 pointers
    # Creates: [0s][1s][2s] with left/right boundaries, mid processes unvisited elements
    # Time: O(n)
    # Space: O(1)
    def sort_colors(self, nums: list[int]) -> None:
        left = mid = 0
        right = len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
