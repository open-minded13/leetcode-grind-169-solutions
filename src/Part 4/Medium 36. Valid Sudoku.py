from typing import List

# Date of Last Practice: Jul 3, 2024
#
# Time Complexity: O(1), since the board size is fixed (9x9) and we are
#                  iterating over each cell once.
#
# Space Complexity: O(1), since we are using additional 27 sets and
#                   each set can contain at most 9 elements.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_size = len(board)
        row_sets = [set() for _ in range(board_size)]
        col_sets = [set() for _ in range(board_size)]
        box_sets = [set() for _ in range(board_size)]

        for row, items in enumerate(board):
            for col, number in enumerate(items):
                number = board[row][col]
                if number == ".":
                    continue

                # Check the current row
                if number in row_sets[row]:
                    return False
                row_sets[row].add(number)

                # Check the current column
                if number in col_sets[col]:
                    return False
                col_sets[col].add(number)

                # Check the current 3x3 box
                box_index = row // 3 * 3 + col // 3
                if number in box_sets[box_index]:
                    return False
                box_sets[box_index].add(number)

        return True


class ThreePassSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_length = len(board)

        # Step 1 - Check each row
        for row in range(board_length):
            row_set = set()
            for number in board[row]:
                if number == ".":
                    continue
                if number not in row_set:
                    row_set.add(number)
                else:
                    return False

        # Step 2 - Check each column
        for col in range(board_length):
            col_set = set()
            for row in range(board_length):
                number = board[row][col]
                if number == ".":
                    continue
                if number not in col_set:
                    col_set.add(number)
                else:
                    return False

        # Step 3 - Check each 3x3 sub-box
        row, col = 0, 0
        while row < board_length:
            box_set = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    number = board[i][j]
                    if number == ".":
                        continue
                    if number not in box_set:
                        box_set.add(number)
                    else:
                        return False

            if col + 3 < board_length:
                col += 3
            else:
                row += 3
                col = 0

        return True


# Test cases
solution = Solution()

board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert solution.isValidSudoku(board1) == True

board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert solution.isValidSudoku(board2) == False

board3 = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]
assert solution.isValidSudoku(board3) == True

board4 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    ["5", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert solution.isValidSudoku(board4) == False

print("All test cases passed!")
