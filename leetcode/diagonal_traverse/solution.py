class Solution:
    """
    Diagonal Traverse Pattern:

    Matrix with coordinates:     d = i+j (diagonal index):
    1(0,0) 2(0,1) 3(0,2)       d=0: 1(0,0)           ↗
    4(1,0) 5(1,1) 6(1,2)       d=1: 2(0,1), 4(1,0)   ↙
    7(2,0) 8(2,1) 9(2,2)       d=2: 3(0,2), 5(1,1), 7(2,0)  ↗
                                d=3: 6(1,2), 8(2,1)   ↙
                                d=4: 9(2,2)           ↗

    'd' = diagonal number = sum of row+col indices (i+j)
    Each diagonal contains elements where i+j equals the same value

    Result: [1,2,4,7,5,3,6,8,9]
    """

    # Time: O(m*n)
    # Space: O(1)
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            if d % 2 == 0:  # up-right diagonal
                for i in range(min(d, m - 1), max(-1, d - n), -1):
                    result.append(mat[i][d - i])
            else:  # down-left diagonal
                for i in range(max(0, d - n + 1), min(d + 1, m)):
                    result.append(mat[i][d - i])

        return result


class SolutionRowShift:
    """
    Row-shift approach: shift each row to align diagonals into columns

    Original matrix:    After shifting rows (col-row=actual_col):
    1 2 3              col=0  col=1  col=2  col=3  col=4
    4 5 6                1      2      3
    7 8 9                       4      5      6
                                       7      8      9
                         ↑      ↓      ↑      ↓      ↑

    Each row is shifted right by its row index, creating vertical columns
    from the original diagonals. Then alternate traversal direction.

    Traverse: 1 → 2,4 → 7,5,3 → 6,8 → 9
    """

    # Time: O(m*n)
    # Space: O(1)
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for col in range(m + n - 1):
            if col % 2 == 1:  # upward
                for row in range(m):
                    i = col - row
                    if 0 <= i < n:
                        result.append(mat[row][i])
            else:  # downward
                for row in range(m - 1, -1, -1):
                    i = col - row
                    if 0 <= i < n:
                        result.append(mat[row][i])

        return result
