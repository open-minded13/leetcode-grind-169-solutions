# Date of Last Practice: Dec 31, 2023 -> Feb 20, 2024
#
# Time Complexity: O(N*M), where N and M are the number of rows and columns in the grid.
#                  Each cell in the M * N grid is visited at most once due to the memoization.
#                  Once a cell is computed, its value is stored and reused in subsequent calls.
#
# Space Complexity: O(min(M, N)), where N and M are the number of rows and columns in the grid.
#                   We are just using a single array to store the number of paths on
#                   different columns of the current row, and
#                   we're overwriting that array as we iterate over the row.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Ensure m is the larger dimension for space optimization
        if m < n:
            m, n = n, m

        # Initialize DP array
        dp = [1] * n

        # Iterate through each cell starting from second last row and column
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[col] += dp[col + 1]

        return dp[0]


class DFS_with_Memoization_Solution:
    # The following has the same time complexity, but the space complexity is O(M*N).
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            if row == m - 1 and col == n - 1:
                dp[row][col] = 1
                return 1

            bottom = dfs(row + 1, col)
            right = dfs(row, col + 1)

            dp[row][col] = bottom + right
            return bottom + right

        return dfs(0, 0)


# Test cases
sol = Solution()
print(sol.uniquePaths(3, 7))  # Output: 28
print(sol.uniquePaths(3, 2))  # Output: 3
