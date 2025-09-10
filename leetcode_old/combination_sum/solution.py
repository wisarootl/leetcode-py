class Solution:
    # Time: O(N^(T/M)) where N=len(candidates), T=target, M=min(candidates)
    # Space: O(T/M) recursion + O(K * T/M) output, where K = number of solutions
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start: int, path: list[int], remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    path.append(candidates[i])
                    backtrack(i, path, remaining - candidates[i])
                    path.pop()

        backtrack(0, [], target)
        return result
