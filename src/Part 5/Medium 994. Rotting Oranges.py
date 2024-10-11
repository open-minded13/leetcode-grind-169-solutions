from collections import deque
from typing import List

# Date of Last Practice: Dec 20, 2023 -> Feb 11, 2024
#
# Time Complexity: O(N*M), where N is the number of rows and M is the number of columns.
#                  Each cell is visited at least once. In the worst case,
#                  each cell in the grid will be visited and processed during
#                  the initial loop and the BFS, resulting O(2*M*N) = O(M*N).
#
# Space Complexity: O(N*M), where N is the number of rows and M is the number of columns.
#                   The worst-case scenario occurs when all oranges are rotten initially,
#                   requiring them to be added to the queue.


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        # Initialize the grid and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))  # Add rotten oranges to the queue

        # BFS
        time_taken = 0
        while queue and fresh_count > 0:
            current_queue_length = len(queue)
            for _ in range(current_queue_length):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 4 directions
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        fresh_count -= 1
                        queue.append((rr, cc))
            time_taken += 1
        return -1 if fresh_count > 0 else time_taken


class Inefficient_BFS_Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs_queue = deque()
        originally_fresh = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bfs_queue.append((i, j, 0))
                if grid[i][j] == 1:
                    originally_fresh.append((i, j))

        time_grid = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while bfs_queue:
            (i, j, time) = bfs_queue.popleft()
            if time_grid[i][j] == -1:
                time_grid[i][j] = time
                for r, c in directions:
                    if (
                        0 <= i + r < len(grid)
                        and 0 <= j + c < len(grid[0])
                        and grid[i + r][j + c] == 1
                    ):
                        grid[i + r][j + c] = 2
                        bfs_queue.append((i + r, j + c, time + 1))

        total_time = 0
        for i, j in originally_fresh:
            if time_grid[i][j] == -1:
                return -1
            if time_grid[i][j] > total_time:
                total_time = time_grid[i][j]

        return total_time


class Inefficient_DFS_Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dfs_roots = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dfs_roots.append((i, j))
                    grid[i][j] = 0
                elif grid[i][j] == 1:
                    grid[i][j] = -1
                elif grid[i][j] == 0:
                    grid[i][j] = -2

        def dfs(root, time):
            (i, j) = root
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return
            if grid[i][j] == -2:
                return
            if 0 <= grid[i][j] < time:
                return
            if grid[i][j] == -1:
                grid[i][j] = time
            if grid[i][j] > time:
                grid[i][j] = time
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for r, c in directions:
                next_orange = (i + r, j + c)
                dfs(next_orange, time + 1)

        for rotten_orange in dfs_roots:
            dfs(rotten_orange, 0)

        total_time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    return -1
                elif grid[i][j] > total_time:
                    total_time = grid[i][j]

        return total_time


class Wrong_DFS_Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dfs_roots = []
        originally_fresh = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dfs_roots.append((i, j))
                    grid[i][j] = 0
                elif grid[i][j] == 1:
                    originally_fresh.append((i, j))
                    grid[i][j] = -1
                elif grid[i][j] == 0:
                    grid[i][j] = -2

        total_time = [0]

        def dfs(root, time):
            (i, j) = root
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return
            if grid[i][j] == -2:
                return
            if 0 <= grid[i][j] < time:
                return
            if grid[i][j] == -1:
                if total_time[0] < time:
                    total_time[0] = time
                grid[i][j] = time
            if grid[i][j] > time:
                # Suppose the current time when oranges A and B
                # are rotten is 4, but you find that A is earlier, at 2.
                # At this point, you'll overwrite B's time, resulting wrong answers.
                if total_time[0] == grid[i][j]:
                    total_time[0] = time

                grid[i][j] = time
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for r, c in directions:
                next_orange = (i + r, j + c)
                dfs(next_orange, time + 1)

        for rotten_orange in dfs_roots:
            dfs(rotten_orange, 0)

        for fresh_orange in originally_fresh:
            (i, j) = fresh_orange
            if grid[i][j] == -1:
                return -1

        return total_time[0]


# Test cases
sol = Solution()
print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # Expected output: 4
print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # Expected output: -1
print(sol.orangesRotting([[0, 2]]))  # Expected output: 0
