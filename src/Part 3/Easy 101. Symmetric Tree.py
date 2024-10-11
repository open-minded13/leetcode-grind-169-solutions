"""
This module provides a solution to determine if a binary tree is symmetric.
The solution is implemented using both recursive and iterative approaches.
"""

from collections import deque
from typing import Optional

# Date of Last Practice: Aug 24, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
#                  We visit each node once.
#
# Space Complexity: O(N), where N is the number of nodes in the binary tree.
#
#                   The space complexity is O(N) because we use a recursive stack
#                   to traverse the tree. In the worst case, the tree is linear,
#                   and the stack can contain all nodes.
#
#                   The iterative approach has a space complexity of O(N) as well
#                   because we use a queue to compare nodes in pairs.
#                   The worst case occurs at the last level of the balanced tree,
#                   where the queue can contain nodes proportional to N/2.
#
#             NOTE: For a binary tree with height `H`, the number of nodes at the last
#                   level is `2^(H-1)` in the worst case. In the queue, each node is
#                   stored as a pair, so the number of pairs will be half of the nodes
#                   in the queue at the worst-case level.


class TreeNode:
    """Represents a node in a binary tree.

    Attributes:
        val: The value of the node.
        left: A reference to the left child node.
        right: A reference to the right child node.
    """

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Determines if a binary tree is symmetric."""

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Determines if the binary tree is symmetric.

        Args:
            root: The root node of the binary tree.

        Returns:
            A boolean indicating whether the tree is symmetric.
        """

        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            """Checks if two subtrees are mirror images of each other."""
            # Step 1 - Base case: If both nodes are None, they are mirrors.
            if not left and not right:
                return True
            # Step 2 - If one of the nodes is None, they are not mirrors.
            if not left or not right:
                return False
            # Step 3 - Check the values of the nodes and recursively check their
            #          children.
            return (
                left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        # Step 4 - Start the recursion from the root's left and right children.
        return is_mirror(root.left, root.right)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """Determines if the binary tree is symmetric using an iterative approach.

        Args:
            root: The root node of the binary tree.

        Returns:
            A boolean indicating whether the tree is symmetric.
        """
        # Step 1 - Use a queue to compare nodes in pairs.
        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()
            # Step 2 - If both nodes are None, continue.
            if not left and not right:
                continue
            # Step 3 - If one node is None or values don't match, return False.
            if not left or not right or left.val != right.val:
                return False
            # Step 4 - Append the children nodes in the appropriate order.
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True


# Test cases
def test_solution():
    """Tests the Solution class for correctness."""
    sol = Solution()

    # Test Case 1: Symmetric tree
    root1 = TreeNode(
        1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
    )
    assert sol.isSymmetric(root1) is True
    assert sol.isSymmetricIterative(root1) is True

    # Test Case 2: Asymmetric tree
    root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert sol.isSymmetric(root2) is False
    assert sol.isSymmetricIterative(root2) is False

    # Test Case 3: Single node (symmetric by definition)
    root3 = TreeNode(1)
    assert sol.isSymmetric(root3) is True
    assert sol.isSymmetricIterative(root3) is True

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
