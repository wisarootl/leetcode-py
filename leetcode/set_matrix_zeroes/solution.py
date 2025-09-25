class Solution:

    # Time: O(m * n)
    # Space: O(1)
    def set_zeroes(self, matrix: list[list[int]]) -> None:
        row_count: int = len(matrix)
        col_count: int = len(matrix[0]) if row_count > 0 else 0

        first_row_has_zero: bool = any(matrix[0][col_index] == 0 for col_index in range(col_count))
        first_col_has_zero: bool = any(matrix[row_index][0] == 0 for row_index in range(row_count))

        for row_index in range(1, row_count):
            for col_index in range(1, col_count):
                if matrix[row_index][col_index] == 0:
                    matrix[row_index][0] = 0
                    matrix[0][col_index] = 0

        for row_index in range(1, row_count):
            for col_index in range(1, col_count):
                if matrix[row_index][0] == 0 or matrix[0][col_index] == 0:
                    matrix[row_index][col_index] = 0

        if first_row_has_zero:
            for col_index in range(col_count):
                matrix[0][col_index] = 0

        if first_col_has_zero:
            for row_index in range(row_count):
                matrix[row_index][0] = 0
