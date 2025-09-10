class Solution:
    # Time: O(n * sum)
    # Space: O(sum)
    def can_partition(self, nums: list[int]) -> bool:
        """
        Example: nums = [1, 5, 11, 5], target = 11

        Initial: dp = [T, F, F, F, F, F, F, F, F, F, F, F]
                      0  1  2  3  4  5  6  7  8  9 10 11

        After num=1: [T, T, F, F, F, F, F, F, F, F, F, F]
                      └─┘ (can make sum 1)

        After num=5: [T, T, F, F, F, T, T, F, F, F, F, F]
                      └─┘          └─┘ └─┘ (can make sums 5,6)

        After num=11:[T, T, F, F, F, T, T, F, F, F, F, T]
                                                        └─┘ (target!)

        Backward iteration prevents using same number twice
        """
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

            # Early termination: found target sum!
            if dp[target]:
                return True

        return False


class SolutionBitset:
    # Time: O(n * sum)
    # Space: O(1)
    def can_partition(self, nums: list[int]) -> bool:
        """
        Example: nums = [1, 5, 11, 5], target = 11

        Bitset representation (bit position = achievable sum):

        Initial:     dp = 1 (binary: 1)
                     Bits: ...0001
                     Sums: {0}

        After num=1: dp |= dp << 1
                     a = dp = 1 (bin: 0001)
                     b = dp << 1 = 2 (bin: 0010)
                     c = a | b = 3 (bin: 0011)
                     Sums: {0, 1}

        After num=5: dp |= dp << 5
                     a = dp = 3 (bin: 0000011)
                     b = dp << 5 = 96 (bin: 1100000)
                     c = a | b = 99 (bin: 1100011)
                     Sums: {0, 1, 5, 6}

        After num=11: dp |= dp << 11
                      a = dp = 99 (bin: 00000001100011)
                      b = dp << 11 = 202752 (bin: 110001100000000)
                      c = a | b = 202851 (bin: 110001101100011)
                      Sums: {0, 1, 5, 6, 11, 12, 16, 17}

        Check: (dp & (1 << 11)) != 0
               a = dp = 202851 (bin: 110001101100011)
               b = 1 << 11 = 2048 (bin: 100000000000)
               c = a & b = 2048 (bin: 100000000000)
               c != 0 → bit 11 is set → True!
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = 1

        for num in nums:
            dp |= dp << num

            # Early termination: found target sum!
            if (dp & (1 << target)) != 0:
                return True

        return False
