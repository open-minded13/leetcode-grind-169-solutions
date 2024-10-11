r"""
Find the in-order successor of a given node in a Binary Search Tree.

This module defines a solution class that provides a method to find the in-order 
successor of a given node in a BST. The in-order successor is defined as the node
with the smallest key greater than the given node's value.

When traversing the tree, every time we check the left subtree, it can be a potential 
successor. For example, if p = 6, during the traversal we update the successor 
with nodes 9, 8, and 7. The final successor is 7.

        9   <--- root
       /
     0
       \
        8   <--- potential successor
       /
      4
     / \ 
    3   7   <--- potential successor and final successor
       /
      6

Typical usage example:

    root = TreeNode(9)
    ...
    solution = Solution()
    successor = solution.inorderSuccessor(root, p)
"""

from typing import Optional

# Date of Last Practice: Oct 1, 2024
#
# Time Complexity: O(H), where H is the height of the binary search tree.
#                  The time complexity is determined by the height of the tree.
#                  In the worst case, the tree is skewed, and the time complexity
#                  is O(N), where N is the number of nodes in the tree.
#                  In the average case, the time complexity is O(log N).
#
# Space Complexity: O(1), as we are using a constant amount of extra space.


class TreeNode:
    """Represents a node in a Binary Search Tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Provides methods to find the in-order successor of a node in a BST."""

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        Find the in-order successor of a given node in the BST.

        Args:
            root: The root of the binary search tree.
            p: The node whose in-order successor is to be found.

        Returns:
            The in-order successor node, or None if there is no successor.
        """
        # Step 1: If `p` has a right child, the successor is the leftmost node
        # in `p`'s right subtree.
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node

        # Step 2: If `p` does not have a right child, traverse the tree from
        # the root and track the potential successor.
        successor = None
        node = root
        while node:
            if node.val > p.val:
                successor = node  # Step 3: Update successor whenever moving left.
                node = node.left
            else:
                node = node.right

        return successor


# Test cases with assertions
def test_inorder_successor():
    # Example 1: root = [2,1,3], p = 1
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    p = root.left
    solution = Solution()
    assert solution.inorderSuccessor(root, p).val == 2

    # Example 2: root = [5,3,6,2,4,null,null,1], p = 6
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    p = root.right
    assert solution.inorderSuccessor(root, p) is None

    # Additional test case: root = [9, 0, null, 8, null, 4, 7, 6], p = 6
    root = TreeNode(9)
    root.left = TreeNode(0)
    root.left.right = TreeNode(8)
    root.left.right.left = TreeNode(4)
    root.left.right.left.left = TreeNode(3)
    root.left.right.left.right = TreeNode(7)
    root.left.right.left.right.left = TreeNode(6)
    p = root.left.right.left.right.left  # p = 6
    assert solution.inorderSuccessor(root, p).val == 7

    print("All test cases passed!")


if __name__ == "__main__":
    test_inorder_successor()
