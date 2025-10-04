from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Optimized version with early termination and word removal.

        Time: O(m*n*4^L) where m*n is board size, L is max word length
        Space: O(W*L) where W is number of words, L is max word length
        """
        if not board or not board[0] or not words:
            return []

        # Build trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        m, n = len(board), len(board[0])
        result = set()

        def dfs(i: int, j: int, node: TrieNode) -> None:
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            char = board[i][j]
            if char not in node.children:
                return

            node = node.children[char]
            if node.word:
                result.add(node.word)
                # Remove word from trie to avoid duplicates
                node.word = None

            # Mark as visited
            board[i][j] = "#"

            # Explore all 4 directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj, node)

            # Restore
            board[i][j] = char

        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return list(result)
