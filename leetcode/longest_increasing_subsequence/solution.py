class Solution:

    # Time: O(n log n)
    # Space: O(n)
    def length_of_lis(self, nums: list[int]) -> int:
        """
        Binary Search + DP: tails[i] = smallest tail of all LIS of length i+1

        Example with middle replacement: [1,5,3,7,2,6,4,8]

        Step | num | tails        | Action
        -----|-----|--------------|------------------
          1  |  1  | [1]          | append
          2  |  5  | [1,5]        | append
          3  |  3  | [1,3]        | replace 5 (pos=1)
          4  |  7  | [1,3,7]      | append
          5  |  2  | [1,2,7]      | replace 3 (pos=1)
          6  |  6  | [1,2,6]      | replace 7 (pos=2)
          7  |  4  | [1,2,4]      | replace 6 (pos=2)
          8  |  8  | [1,2,4,8]    | append

        Result: len(tails) = 4
        """
        import bisect

        tails: list[int] = []

        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)
