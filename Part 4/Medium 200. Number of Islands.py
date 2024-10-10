"""Solution for counting the number of islands in a binary grid.

This module implements a class and method to solve the LeetCode problem 200,
'Number of Islands'. The class Solution contains a function numIslands that
takes a binary grid as input and returns the number of distinct islands by
using Depth-First Search (DFS) to explore adjacent lands.
"""

# Date of Last Practice: Dec 15, 2023 -> Feb 7, 2024 -> Oct 9, 2024
#
# Time Complexity: O(M * N), where M is the number of rows and N is the number of
#                  columns. Each cell is visited once.
#
# Space Complexity: O(M * N), where M is the number of rows and N is the number of
#                   columns. In the worst case, if all land cells are connected
#                   (i.e., a large island spanning the entire grid), the recursion
#                   stack can grow up to M * N.


from typing import List


class Solution:
    """Counts the number of islands in a 2D binary grid.

    An island is formed by adjacent lands ('1') connected either horizontally
    or vertically. The grid's edges are assumed to be surrounded by water ('0').

    Attributes:
        grid (List[List[str]]): The binary grid where '1' is land and '0' is water.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """Returns the number of islands in the given grid.

        This function implements a depth-first search (DFS) to explore all lands
        ('1's) in the grid, marking visited cells as '0'. It increases the count
        of islands each time a new unvisited land cell is found.

        Args:
            grid: A 2D list representing the grid with '1's (land) and '0's (water).

        Returns:
            int: The number of distinct islands found in the grid.
        """
        if not grid:
            return 0

        row_length, col_length = len(grid), len(grid[0])

        def dfs(i, j):
            # If the current cell is out of bounds or not land, return immediately.
            if (
                i < 0
                or j < 0
                or i >= row_length
                or j >= col_length
                or grid[i][j] == "0"
            ):
                return
            grid[i][j] = "0"  # Mark the current land as visited (set to water).
            # Visit all four directions (up, down, left, right).
            dfs(i + 1, j)  # Visit the cell below.
            dfs(i - 1, j)  # Visit the cell above.
            dfs(i, j + 1)  # Visit the cell to the right.
            dfs(i, j - 1)  # Visit the cell to the left.

        island_count = 0  # Initialize the number of islands to 0.
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == "1":  # Found an unvisited piece of land.
                    dfs(i, j)  # Perform DFS to mark all connected lands.
                    island_count += 1  # Increment the island count.

        return island_count


def main():
    """Runs test cases for the Solution class's numIslands function."""
    # Step 1 - Create an instance of the Solution class.
    solution = Solution()

    # Step 2 - Define test cases.
    test_case_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    test_case_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    test_case_3 = []  # Empty grid edge case.
    test_case_4 = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]  # No land edge case.
    test_case_5 = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"],
    ]  # Entire grid is one large island.

    # Step 3 - Run assertions to validate the results.
    assert solution.numIslands(test_case_1) == 1, "Test Case 1 Failed"
    assert solution.numIslands(test_case_2) == 3, "Test Case 2 Failed"
    assert solution.numIslands(test_case_3) == 0, "Test Case 3 Failed"
    assert solution.numIslands(test_case_4) == 0, "Test Case 4 Failed"
    assert solution.numIslands(test_case_5) == 1, "Test Case 5 Failed"

    print("All test cases passed.")


if __name__ == "__main__":
    main()
