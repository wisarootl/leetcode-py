class Solution:

    # Time: O(n)
    # Space: O(n)
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        answers: list[list[int]] = []

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                answer = [seen[complement], i]
                answers.append(answer)
            seen[num] = i

        if len(answers) > 1:
            raise ValueError(f"Found {len(answers)} answers in the solution: {answers}")

        return answers[0] if answers else []
