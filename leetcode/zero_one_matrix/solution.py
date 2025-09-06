from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def update_matrix(self, mat: list[list[int]]) -> list[list[int]]:
        UNSEEN = -1
        m, n = len(mat), len(mat[0])
        queue: deque[tuple[int, int]] = deque()

        # Mark 1s as UNSEEN and add all 0s to queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = UNSEEN

        # BFS from all 0s simultaneously
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] == UNSEEN:
                    mat[r][c] = mat[row][col] + 1
                    queue.append((r, c))

        return mat
