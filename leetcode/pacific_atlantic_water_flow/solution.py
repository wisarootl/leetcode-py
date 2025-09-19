class Solution:

    # Time: O(m * n)
    # Space: O(m * n)
    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific: set[tuple[int, int]] = set()
        atlantic: set[tuple[int, int]] = set()

        def dfs(r: int, c: int, visited: set) -> None:
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # DFS from Pacific borders (top and left)
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)

        # DFS from Atlantic borders (bottom and right)
        for i in range(m):
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(m - 1, j, atlantic)

        return [[r, c] for r, c in pacific & atlantic]
