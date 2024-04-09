from typing import Optional

# Date of Last Practice: Mar 13, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the binary search tree (BST).
#                  In the worst-case scenario, the algorithm might
#                  need to visit every node in the tree once.
#
# Space Complexity: O(H), where H is the height of the tree.
#                   This space is used by the call stack
#                   during the recursive traversal of the tree.
#                   In the worst-case scenario (a degenerate tree),
#                   the space complexity can become O(N).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Helper function to perform DFS and sum values within range
        def _range_sum(node):
            if node is None:  # Base case: Node is null
                return
            if low <= node.val <= high:  # Node value is within range
                self.sum += node.val
                _range_sum(node.left)  # Check left subtree
                _range_sum(node.right)  # Check right subtree
            elif node.val < low:  # Node value is less than range, skip left subtree
                _range_sum(node.right)
            elif (
                node.val > high
            ):  # Node value is greater than range, skip right subtree
                _range_sum(node.left)

        _range_sum(root)  # Initialize DFS from root
        return self.sum


# Test cases
solution = Solution()

# Test case 1
root1 = TreeNode(
    10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))
)
assert solution.rangeSumBST(root1, 7, 15) == 32, "Test case 1 failed"

# Reset sum for the next test
solution.sum = 0

# Test case 2
root2 = TreeNode(
    10,
    TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, None, TreeNode(6))),
    TreeNode(15, TreeNode(13), TreeNode(18)),
)
assert solution.rangeSumBST(root2, 6, 10) == 23, "Test case 2 failed"

print("All test cases passed!")
