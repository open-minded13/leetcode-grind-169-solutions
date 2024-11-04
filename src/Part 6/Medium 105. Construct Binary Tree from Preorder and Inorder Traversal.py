"""Construct a binary tree from preorder and inorder traversal data.

Given two integer arrays representing the preorder and inorder traversal
of a binary tree, reconstruct and return the binary tree.

Typical usage example:

    solution = Solution()
    tree = solution.buildTree(preorder, inorder)
"""

from typing import List, Optional
from collections import deque

# Date of Last Practice: Jan 1, 2024 -> Feb 20, 2024 -> Nov 3, 2024
#
# Time Complexity: O(N), where N is the number of nodes.
#                  - Creating the hashmap (inorder_index_map) takes O(N) time.
#                  - The find_subtree function is called once for each node in the tree.
#                  - For each call, the operations performed (like looking up in the
#                    hashmap and creating a new TreeNode) take O(1) time.
#                  - Therefore, the overall time complexity is O(N).
#
# Space Complexity: O(N), where N is the number of nodes.
#                   - The space complexity for the hashmap is O(N).
#                   - The space complexity of the recursion stack is O(H),
#                     where H is the height of the tree.
#                   - In the worst case (a skewed tree), h can be O(N),
#                     but in a balanced tree, it would be O(log N).
#                   - Overall, it is dominated by building hashmap, O(N).


class TreeNode:
    """Binary tree node with a value and optional left and right children."""

    def __init__(self, val=0, left=None, right=None):
        """Initialize the TreeNode with a value, left, and right child nodes.

        Args:
            val (int): Value of the node.
            left (TreeNode): Left child node.
            right (TreeNode): Right child node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Construct a binary tree from preorder and inorder traversal arrays."""

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Constructs and returns the binary tree root from preorder and inorder.

        Args:
            preorder (List[int]): Preorder traversal of the tree.
            inorder (List[int]): Inorder traversal of the tree.

        Returns:
            TreeNode: Root node of the constructed binary tree.
        """
        # Step 1 - Create a hashmap to quickly find indices in inorder array
        find_pivot = {value: index for index, value in enumerate(inorder)}
        preorder = deque(preorder)  # Convert preorder to deque for O(1) popleft

        # Step 2 - Recursive function to construct tree
        def find_subtree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Step 3 - Get the current root value and corresponding node
            cur_val = preorder.popleft()
            pivot = find_pivot[cur_val]

            # Step 4 - Recursively build the left and right subtrees
            node = TreeNode(cur_val)
            node.left = find_subtree(left, pivot - 1)
            node.right = find_subtree(pivot + 1, right)

            return node

        # Step 5 - Start the recursive tree construction from the full inorder range
        return find_subtree(0, len(inorder) - 1)


# Helper function for testing - get inorder traversal of the tree
def get_inorder(node: Optional[TreeNode]) -> List[int]:
    """Returns the inorder traversal of the binary tree as a list.

    Args:
        node (TreeNode): The root of the binary tree.

    Returns:
        List[int]: List of node values in inorder traversal.
    """
    return get_inorder(node.left) + [node.val] + get_inorder(node.right) if node else []


def main():
    """Main function to demonstrate the construction of a binary tree."""
    solution = Solution()

    # Test Case 1
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    tree1 = solution.buildTree(preorder1, inorder1)
    assert get_inorder(tree1) == inorder1, "Test Case 1 Failed"

    # Test Case 2
    preorder2 = [-1]
    inorder2 = [-1]
    tree2 = solution.buildTree(preorder2, inorder2)
    assert get_inorder(tree2) == inorder2, "Test Case 2 Failed"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
