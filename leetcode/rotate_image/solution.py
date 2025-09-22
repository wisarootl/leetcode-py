class Solution:

    # Time: O(n²)
    # Space: O(1)
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
