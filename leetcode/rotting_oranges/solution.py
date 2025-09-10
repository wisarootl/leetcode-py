from collections import deque


class Solution:
    # Time: O(m*n)
    # Space: O(m*n)
    def oranges_rotting(self, grid: list[list[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        _ = EMPTY

        m, n = len(grid), len(grid[0])
        queue: deque[tuple[int, int]] = deque()
        fresh = 0

        # Find all rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == FRESH:
                        grid[nx][ny] = ROTTEN
                        fresh -= 1
                        queue.append((nx, ny))

            if queue:
                minutes += 1

        return minutes if fresh == 0 else -1
