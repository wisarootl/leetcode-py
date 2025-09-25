class Solution:

    # Time: O(n)
    # Space: O(1)
    def num_decodings(self, s: str) -> int:
        if not s:
            return 0

        num_ways_two_steps_behind: int = 1
        num_ways_one_step_behind: int = 0 if s[0] == "0" else 1

        for index in range(1, len(s)):
            current_char: str = s[index]
            previous_char: str = s[index - 1]

            current_num_ways: int = 0

            if current_char != "0":
                current_num_ways += num_ways_one_step_behind

            two_digit_value: int = int(previous_char + current_char)
            if previous_char != "0" and 10 <= two_digit_value <= 26:
                current_num_ways += num_ways_two_steps_behind

            num_ways_two_steps_behind, num_ways_one_step_behind = (
                num_ways_one_step_behind,
                current_num_ways,
            )

        return num_ways_one_step_behind
