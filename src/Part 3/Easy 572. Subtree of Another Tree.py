"""
Determine if one binary tree is a subtree of another.

This module defines a class `Solution` with a method `isSubtree` that checks
if `subRoot` is a subtree of `root`.
"""

# Date of Last Practice: Sep 10, 2024
#
# Time Complexity: O(N * M), where N is the number of nodes in the main tree
#                  and M is the number of nodes in the subtree.
#
#                  In the worst case, we may have to use each node in the main
#                  tree to check if it is the same as the subtree. This results
#                  in a time complexity of O(N * M).
#
# Space Complexity: O(H), where H is the height of the main tree.
#                   The space complexity is determined by the recursive calls
#                   made to check if the subtree is the same as the main tree.
#
#                   In the worst case, the space complexity is O(N) for a skewed
#                   tree, where N is the number of nodes in the main tree.
#
#                   For a balanced tree, the space complexity is O(log N).


# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): Value of the node.
        left (TreeNode): Left child of the node.
        right (TreeNode): Right child of the node.
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a binary tree node.

        Args:
            val (int): Value of the node.
            left (TreeNode, optional): Left child node. Defaults to None.
            right (TreeNode, optional): Right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Provides a solution to check if one binary tree is a subtree of another.
    """

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        Checks if subRoot is a subtree of root.

        Args:
            root (TreeNode): The root of the main tree.
            subRoot (TreeNode): The root of the subtree to check.

        Returns:
            bool: True if subRoot is a subtree of root, otherwise False.
        """

        def is_the_same(node: TreeNode, sub_node: TreeNode) -> bool:
            # Step 1 - Check if both nodes are None
            if not node and not sub_node:
                return True
            # Step 2 - If one node is None and the other is not, return False
            if not node or not sub_node:
                return False
            # Step 3 - Compare the current node values and recursively check children
            if node.val != sub_node.val:
                return False
            return is_the_same(node.left, sub_node.left) and is_the_same(
                node.right, sub_node.right
            )

        def find_subroot(node: TreeNode) -> bool:
            # Step 4 - Base case: If node is None, return False
            if not node:
                return False
            # Step 5 - Check if the current node is the same as subRoot
            if is_the_same(node, subRoot):
                return True
            # Step 6 - Recursively check left and right subtrees
            return find_subroot(node.left) or find_subroot(node.right)

        return find_subroot(root)


# Test cases
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)

    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)

    assert Solution().isSubtree(root1, subRoot1) is True, "Test Case 1 Failed"

    # Test Case 2
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)

    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    subRoot2.right = TreeNode(2)

    assert Solution().isSubtree(root2, subRoot2) is False, "Test Case 2 Failed"

    print("All test cases passed!")
