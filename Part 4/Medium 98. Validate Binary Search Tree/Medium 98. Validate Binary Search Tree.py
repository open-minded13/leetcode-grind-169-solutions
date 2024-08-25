"""Validate whether a binary tree is a valid Binary Search Tree (BST).

This module defines a TreeNode class representing nodes in a binary tree and a
Solution class with a method to validate if a binary tree is a valid BST. It
also includes helper functions and test cases.
"""

import sys

# Date of Last Practice: Dec 12, 2023 -> Feb 7, 2024 -> Aug 24, 2024

# Time Complexity: O(N), where N is the number of nodes in the tree.
#                  The algorithm performs a depth-first traversal of the binary tree.
#                  During this traversal, it visits every node exactly once.

# Space Complexity: O(N), where N is the number of nodes in the tree.
#                   For a skewed tree (worst case), the space complexity is O(N).
#                   For a balanced tree, the space complexity is O(log N).


class TreeNode:
    """Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node.
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
    """

    def __init__(self, val=0, left=None, right=None):
        """Initializes a TreeNode with a value and optional left/right children.

        Args:
            val (int): The value of the node.
            left (TreeNode): The left child node. Default is None.
            right (TreeNode): The right child node. Default is None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Validate if a binary tree is a valid Binary Search Tree."""

    def isValidBST(self, root: TreeNode) -> bool:
        """Validates whether a given binary tree is a valid BST.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            bool: True if the tree is a valid BST, False otherwise.
        """

        def isValid(node, min_value, max_value):
            """Helper function to recursively validate the BST property.

            Args:
                node (TreeNode): The current node being checked.
                min_value (int): The minimum allowable value for the current node.
                max_value (int): The maximum allowable value for the current node.

            Returns:
                bool: True if the subtree rooted at node is a valid BST.
            """
            # Step 1 - Base case: An empty subtree is a valid BST.
            if node is None:
                return True

            # Step 2 - Check if the current node's value violates the BST property.
            if node.val <= min_value or node.val >= max_value:
                return False

            # Step 3 - Recursively validate the left and right subtrees.
            is_valid_left = isValid(node.left, min_value, node.val)
            is_valid_right = isValid(node.right, node.val, max_value)

            # Step 4 - Return True if both subtrees are valid, otherwise False.
            return is_valid_left and is_valid_right

        # Step 5 - Initialize recursion with the full allowable range for the root.
        return isValid(root, -sys.maxsize - 1, sys.maxsize)


def buildTree(nodes, index=0):
    """Builds a binary tree from a list representation.

    Args:
        nodes (list): List representing the binary tree (None for empty nodes).
        index (int): The current index in the list. Default is 0.

    Returns:
        TreeNode: The root node of the constructed binary tree.
    """
    # Step 1 - Base case: If index is out of range or node is None, return None.
    if index >= len(nodes) or nodes[index] is None:
        return None

    # Step 2 - Create the current node.
    node = TreeNode(nodes[index])

    # Step 3 - Recursively build the left and right subtrees.
    node.left = buildTree(nodes, 2 * index + 1)
    node.right = buildTree(nodes, 2 * index + 2)

    # Step 4 - Return the current node.
    return node


if __name__ == "__main__":
    # Main function to test the Solution with provided test cases.

    sol = Solution()

    # Test case 1: The tree [2, 1, 3] is a valid BST.
    tree1 = buildTree([2, 1, 3])
    assert sol.isValidBST(tree1) is True, "Test case 1 failed"

    # Test case 2: The tree [5, 1, 4, None, None, 3, 6] is not a valid BST.
    tree2 = buildTree([5, 1, 4, None, None, 3, 6])
    assert sol.isValidBST(tree2) is False, "Test case 2 failed"

    print("All test cases passed!")
