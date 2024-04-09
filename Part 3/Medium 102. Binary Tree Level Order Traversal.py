from collections import deque
from typing import List, Optional

# Date of Last Practice: Nov 13, 2023 -> Feb 3, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
#
# Space Complexity: O(N), where N is the number of nodes in the binary tree.
#                   In the worst case, the maximum number of nodes at any level is N/2
#                   (for a completely balanced binary tree),
#                   where N is the total number of nodes.
#                   Therefore, the space complexity is O(N/2) ≈ O(N).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFS_Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            current_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result


class DFS_Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, level, result):
            if root:
                if len(result) <= level:
                    result.append([])
                result[level].append(root.val)
                dfs(root.left, level + 1, result)
                dfs(root.right, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result


def test_bfs_solution():
    # Test Case 1: Balanced Binary Tree
    #     1
    #    / \
    #   2   3
    #  / \ / \
    # 4  5 6  7
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3, TreeNode(6), TreeNode(7))

    solution = BFS_Solution()
    result1 = solution.levelOrder(root1)
    assert result1 == [[1], [2, 3], [4, 5, 6, 7]], f"Test Case 1 Failed: {result1}"

    # Test Case 2: Unbalanced Binary Tree
    #     1
    #      \
    #       2
    #        \
    #         3
    root2 = TreeNode(1)
    root2.right = TreeNode(2, right=TreeNode(3))

    result2 = solution.levelOrder(root2)
    assert result2 == [[1], [2], [3]], f"Test Case 2 Failed: {result2}"

    # Test Case 3: Empty Tree
    result3 = solution.levelOrder(None)
    assert result3 == [], f"Test Case 3 Failed: {result3}"

    print("All test cases passed!")


# Run the test cases
test_bfs_solution()
