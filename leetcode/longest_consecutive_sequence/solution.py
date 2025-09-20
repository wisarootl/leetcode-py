class Solution:

    # Time: O(n) - each number visited at most twice (once as start, once as continuation)
    # Space: O(n) - hash set storage
    def longest_consecutive(self, nums: list[int]) -> int:
        """
        Find longest consecutive sequence using hash set.

        Example: nums = [100, 4, 200, 1, 3, 2]

        Step 1: Create set {100, 4, 200, 1, 3, 2}

        Step 2: For each number, check if it's sequence start (num-1 not in set):

        num=100: 99 not in set → START sequence
        100 → 101 not in set → length=1

        num=4: 3 in set → SKIP (not start)

        num=200: 199 not in set → START sequence
        200 → 201 not in set → length=1

        num=1: 0 not in set → START sequence
        1 → 2 in set → 2 → 3 in set → 3 → 4 in set → 4 → 5 not in set
        Sequence: [1,2,3,4] → length=4 ✓

        Result: max(1, 1, 4) = 4
        """
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
