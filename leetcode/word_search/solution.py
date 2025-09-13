from collections import Counter


class Solution:

    # Time: O(m*n*4^L) where L is word length
    # Space: O(L)
    def exist(self, board: list[list[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        # Early pruning: check if board has enough characters
        board_counter = Counter(ch for row in board for ch in row)
        word_counter = Counter(word)
        for ch in word_counter:
            if board_counter[ch] < word_counter[ch]:
                return False

        # Optimization: start from less frequent end
        if board_counter[word[0]] > board_counter[word[-1]]:
            word = word[::-1]

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if dfs(i + di, j + dj, k + 1):
                    board[i][j] = temp
                    return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
