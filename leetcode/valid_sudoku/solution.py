class Solution:

    # Time: O(1) - fixed 9x9 board
    # Space: O(1) - fixed size sets
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        rows: list[set[str]] = [set() for _ in range(9)]
        cols: list[set[str]] = [set() for _ in range(9)]
        boxes: list[list[set[str]]] = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]

                    if num in rows[i] or num in cols[j] or num in boxes[i // 3][j // 3]:
                        return False

                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[i // 3][j // 3].add(num)

        return True
