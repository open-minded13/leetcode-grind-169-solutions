from typing import Optional, List
from collections import deque, defaultdict
import sys

# Date of Last Practice: Mar 7, 2024
#
# Time Complexity: O(N), where N is the total number of nodes.
#                  We use breadth-first search to traverse each node once.
#
# Space Complexity: O(N), where N is the total number of nodes.
#                   In the case of a balanced binary tree,
#                   the largest breadth level could indeed have about N/2 nodes,
#                   leading to a space complexity for the queue of O(N).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: "Optional[TreeNode]") -> "List[List[int]]":
        if not root:
            return []

        queue = deque([(0, root)])
        vertical_node_val = defaultdict(list)
        smallest_col = sys.maxsize
        largest_col = -sys.maxsize - 1

        while queue:
            for _ in range(len(queue)):
                column, node = queue.popleft()
                if node.left:
                    queue.append((column - 1, node.left))
                if node.right:
                    queue.append((column + 1, node.right))
                vertical_node_val[column].append(node.val)

                smallest_col = min(smallest_col, column)
                largest_col = max(largest_col, column)

        return [
            vertical_node_val[column] for column in range(smallest_col, largest_col + 1)
        ]


# Test cases
def test_solution():
    sol = Solution()

    # Test case 1
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.verticalOrder(root1) == [[9], [3, 15], [20], [7]]

    # Test case 2
    root2 = TreeNode(
        3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7))
    )
    assert sol.verticalOrder(root2) == [[4], [9], [3, 0, 1], [8], [7]]

    # Test case 3
    root3 = TreeNode(
        3,
        TreeNode(9, TreeNode(4), TreeNode(0, None, TreeNode(2))),
        TreeNode(8, TreeNode(1, TreeNode(5)), TreeNode(7)),
    )
    assert sol.verticalOrder(root3) == [[4], [9, 5], [3, 0, 1], [8, 2], [7]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
