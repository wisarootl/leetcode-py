class Solution:
    # Time: O(m*n)
    # Space: O(m*n)
    def flood_fill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original:
                return
            image[r][c] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image
