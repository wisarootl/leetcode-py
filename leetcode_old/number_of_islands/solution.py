class Solution:
    # Time: O(m * n) where m = rows, n = cols
    # Space: O(m * n) for recursion stack in worst case
    def num_islands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        VISITED = "0"
        UNVISITED_ISLAND = "1"

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != UNVISITED_ISLAND:
                return

            grid[r][c] = VISITED
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == UNVISITED_ISLAND:
                    islands += 1
                    dfs(r, c)

        return islands
