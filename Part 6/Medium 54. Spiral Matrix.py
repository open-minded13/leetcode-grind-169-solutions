from typing import List

# Date of Last Practice: Dec 31, 2023 -> Feb 18, 2024
#
# Time Complexity: O(N*M), where N and M are the number of rows and columns in the matrix.
#                  Given an m x n matrix, each element is visited once.
#
# Space Complexity: O(N*M), where N and M are the number of rows and columns in the matrix.
#                   This is because of the output list. Apart from this,
#                   we only use constant extra space, including top, bottom, left, and right.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        output = []
        while left <= right and top <= bottom:
            # Traverse from left to right
            for col in range(left, right + 1):
                output.append(matrix[top][col])
            top += 1

            # Traverse downwards
            for row in range(top, bottom + 1):
                output.append(matrix[row][right])
            right -= 1

            if left <= right and top <= bottom:
                # Traverse from right to left
                for col in range(right, left - 1, -1):
                    output.append(matrix[bottom][col])
                bottom -= 1

                # Traverse upwards
                for row in range(bottom, top - 1, -1):
                    output.append(matrix[row][left])
                left += 1

        return output


class First_Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_ptr = 0
        row, col = 0, 0
        row_length, col_length = len(matrix), len(matrix[0])
        visited = -101

        output = []
        while True:
            output.append(matrix[row][col])
            matrix[row][col] = visited

            all_dir_checker = 0
            if (
                row + 1 < row_length and matrix[row + 1][col] == visited
            ) or row + 1 >= row_length:
                all_dir_checker += 1
            if (row - 1 >= 0 and matrix[row - 1][col] == visited) or row - 1 < 0:
                all_dir_checker += 1
            if (
                col + 1 < col_length and matrix[row][col + 1] == visited
            ) or col + 1 >= col_length:
                all_dir_checker += 1
            if (col - 1 >= 0 and matrix[row][col - 1] == visited) or col - 1 < 0:
                all_dir_checker += 1
            if all_dir_checker == 4:
                return output

            while True:
                r, c = directions[direction_ptr]
                if (
                    0 <= row + r < row_length
                    and 0 <= col + c < col_length
                    and matrix[row + r][col + c] == visited
                ):
                    direction_ptr = direction_ptr + 1 if direction_ptr + 1 < 4 else 0
                elif not (0 <= row + r < row_length and 0 <= col + c < col_length):
                    direction_ptr = direction_ptr + 1 if direction_ptr + 1 < 4 else 0
                else:
                    row, col = row + r, col + c
                    break


solution = Solution()

# Test case 1
assert solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    1,
    2,
    3,
    6,
    9,
    8,
    7,
    4,
    5,
]

# Test case 2
assert solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
    1,
    2,
    3,
    4,
    8,
    12,
    11,
    10,
    9,
    5,
    6,
    7,
]

# Test case 3: Single row
assert solution.spiralOrder([[1, 2, 3, 4, 5]]) == [1, 2, 3, 4, 5]

# Test case 4: Single column
assert solution.spiralOrder([[1], [2], [3], [4], [5]]) == [1, 2, 3, 4, 5]

print("All test cases passed!")
