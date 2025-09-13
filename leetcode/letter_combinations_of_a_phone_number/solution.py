class Solution:

    # Time: O(4^n)
    # Space: O(4^n)
    def letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(i: int, path: str) -> None:
            if i == len(digits):
                result.append(path)
                return

            for letter in phone[digits[i]]:
                backtrack(i + 1, path + letter)

        backtrack(0, "")
        return result
