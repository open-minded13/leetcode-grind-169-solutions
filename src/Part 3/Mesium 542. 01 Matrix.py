from typing import List
from collections import deque
import sys

# Date of Last Practice: Nov 25, 2023 -> Feb 4, 2024
#
# Time Complexity: O(M * N), where M and N are the number of rows and columns in the matrix.
#                  This is because each cell is visited once.
#
# Space Complexity: O(M * N), where M and N are the number of rows and columns in the matrix.
#                   This is because, in the worst case, the queue will be filled with
#                   all cells in the matrix.


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        queue = deque()
        rows, cols = len(mat), len(mat[0])

        # Initialize the queue with 0s and mark 1s as sys.maxsize
        # max_int = sys.maxsize = 2^61
        # min_int = -sys.maxsize - 1 = -2^61 - 1
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    mat[i][j] = sys.maxsize
                else:
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] > mat[i][j] + 1:
                    mat[ni][nj] = mat[i][j] + 1
                    queue.append((ni, nj))

        return mat


# Test cases
sol = Solution()
mat1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert sol.updateMatrix(mat1) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

mat2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
assert sol.updateMatrix(mat2) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

mat3 = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
assert sol.updateMatrix(mat3) == [[4, 3, 2], [3, 2, 1], [2, 1, 0]]

print("All test cases passed!")
