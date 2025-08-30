class Solution:
    # Time: O(m*n)
    # Space: O(1)
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        # Check if all rows have same length
        cols = len(matrix[0])
        for row in matrix:
            if len(row) != cols:
                raise ValueError("Invalid matrix: all rows must have same length")

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            # Right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # Down
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # Left (if still valid row)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # Up (if still valid column)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
