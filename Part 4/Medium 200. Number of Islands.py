from typing import List

# Date of Last Practice: Dec 15, 2023 -> Feb 7, 2024
#
# Time Complexity: O(M * N), where M is the number of rows and N is the number of columns.
#                  Each cell is visited once.
#
# Space Complexity: O(M * N), where M is the number of rows and N is the number of columns.
#                   This is because, in the worst case, the call stack in DFS
#                   will contain all cells in the given grid.
#                   However, this is typically less in practice since not all cells
#                   will be part of the recursion at the same time.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count


# Test cases
sol = Solution()

# Test case 1
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print("Test Case 1:", sol.numIslands(grid1))  # Expected output: 1

# Test case 2
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print("Test Case 2:", sol.numIslands(grid2))  # Expected output: 3

# Test case 3 (Edge case: empty grid)
grid3 = []
print("Test Case 3:", sol.numIslands(grid3))  # Expected output: 0

# Test case 4 (Edge case: no land)
grid4 = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
print("Test Case 4:", sol.numIslands(grid4))  # Expected output: 0

# Test case 5 (Edge case: all land)
grid5 = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]
print("Test Case 5:", sol.numIslands(grid5))  # Expected output: 1
