class Solution:
    # Time: O(n^2)
    # Space: O(k) where k is number of unique triplets
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return [list(triplet) for triplet in result]
