# Date of Last Practice: Jan 9, 2024 -> Feb 22, 2024
#
# Time Complexity: O(N*M*4^K), where N is the number of rows, M is the number of columns,
#                  and K is length of the word. In the worst case,
#                  we may have to explore all possible paths to find the word.
#                  For each cell, we explore at most four directions,
#                  so the time complexity of the DFS search is O(4^K),
#                  where K is the length of the word.
#
# Space Complexity: O(K) or O(M*N), where N is the number of rows, M is the number of columns,
#                   and K is length of the word. Typically, the depth of a recursive stack is O(K).
#                   However, sometimes in the worst case,
#                   when each cell is the source of depth-first search,
#                   we will need to iterate M*N elements.


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dfs_sources = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs_sources.append((i, j))

        self.is_found = False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        current_checking_path = set()

        def dfs(row, col, index):
            if (
                not (
                    0 <= row < len(board)
                    and 0 <= col < len(board[0])
                    and (row, col) not in current_checking_path
                )
                or board[row][col] != word[index]
            ):
                return
            if index == len(word) - 1:
                self.is_found = True
                return

            current_checking_path.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, index + 1)
            current_checking_path.remove((row, col))

        for row, col in dfs_sources:
            dfs(row, col, 0)

        return self.is_found


class SameSolution:
    # This is the version I used on Jan 8, 2023,
    # but I like the new version above because it is cleaner and easier to debug.

    def exist(self, board: List[List[str]], word: str) -> bool:
        dfs_sources = []
        row_length = len(board)
        col_length = len(board[0])
        for i in range(row_length):
            for j in range(col_length):
                if board[i][j] == word[0]:
                    dfs_sources.append((i, j))

        visited = [[False for _ in range(col_length)] for _ in range(row_length)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(source, cur_level):
            if cur_level == len(word):
                return False

            (row, col) = source
            if board[row][col] == word[cur_level]:
                if cur_level == len(word) - 1:
                    return True

                visited[row][col] = True
                word_exists = False
                for r, c in directions:
                    if (
                        0 <= row + r < row_length
                        and 0 <= col + c < col_length
                        and visited[row + r][col + c] == False
                    ):
                        word_exists = (
                            dfs((row + r, col + c), cur_level + 1) or word_exists
                        )
                visited[row][col] = False
                return word_exists
            else:
                return False

        for source in dfs_sources:
            if dfs(source, 0):
                return True

        return False


# Test cases
sol = Solution()

# Provided test cases
assert (
    sol.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
    == True
)
assert (
    sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    == True
)
assert (
    sol.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
    == False
)

# Additional test cases
assert sol.exist([["A"]], "A") == True  # Single cell, matching word
assert (
    sol.exist([["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"]], "AAAA") == True
)  # Word formed in a square
assert (
    sol.exist([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]], "AEI") == False
)  # Non-adjacent cells

print("All test cases passed!")
