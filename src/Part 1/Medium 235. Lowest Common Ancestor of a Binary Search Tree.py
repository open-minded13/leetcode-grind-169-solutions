from typing import List

# Date of Last Practice: Oct 22, 2023 -> Jan 29, 2024
#
# Time Complexity: O(H), where H is the height of the binary search tree.
#                  In the worst case, the tree can be skewed (all nodes in a single branch),
#                  which would result in a time complexity of O(n), where n is the number of nodes in the tree.
#                  However, in the average case, for a balanced BST, the height (h) is approximately log2(n).
#                  Therefore, the time complexity is typically O(log n) in average and best cases.
# Space Complexity: O(1) because the solution uses no additional data structures like a stack for recursion.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            if root.val < min(p.val, q.val):
                root = root.right
                continue
            if root.val > max(p.val, q.val):
                root = root.left
                continue
            return root


# Test Cases
if __name__ == "__main__":
    # Create a sample tree for testing
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    solution = Solution()

    # Test Case 1: p = 2, q = 8
    # The lowest common ancestor should be 6
    result = solution.lowestCommonAncestor(root, root.left, root.right)
    assert result.val == 6

    # Test Case 2: p = 2, q = 4
    # The lowest common ancestor should be 2
    result = solution.lowestCommonAncestor(root, root.left, root.left.right)
    assert result.val == 2

    # Test Case 3: p = 2, q = 5
    # The lowest common ancestor should be 2
    result = solution.lowestCommonAncestor(root, root.left, root.left.right.right)
    assert result.val == 2

    print("All test cases passed!")
