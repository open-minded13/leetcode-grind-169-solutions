"""
A module to convert a sorted integer array into a height-balanced binary 
search tree (BST).

This module provides a class `Solution` with a method `sortedArrayToBST` 
to convert a sorted array into a height-balanced BST. The method is tested 
using several assert statements.
"""

from typing import List, Optional

# Date of Last Practice: Aug 27, 2024
#
# Time Complexity: O(N), where N is the number of elements in the input list nums.
#                  The function builds the entire binary search tree by visiting each
#                  element in the list once.
#
# Space Complexity: O(N), where N is the number of elements in the input list nums.
#                   The function uses recursion to build the binary search tree, which
#                   requires additional space on the call stack. The maximum depth of
#                   the recursion is the height of the binary search tree, which is
#                   O(log N) for a balanced tree and O(N) for an unbalanced tree.


class TreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        """
        Initializes a TreeNode with a value and optional left and right children.

        Args:
            val: The value of the node.
            left: Reference to the left child node.
            right: Reference to the right child node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Provides a method to convert a sorted array into a height-balanced BST.
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted array into a height-balanced binary search tree.

        Args:
            nums: A list of integers sorted in ascending order.

        Returns:
            A TreeNode representing the root of the height-balanced BST.
        """

        def build_tree(cur_nums: List[int]) -> Optional[TreeNode]:
            """
            Recursively builds the tree from the sorted array.

            Args:
                cur_nums: A sublist of integers from which to build the BST.

            Returns:
                A TreeNode representing the root of the BST for this sublist.
            """
            # Base case: empty list returns None
            if not cur_nums:
                return None

            # Step 1: Find the middle index and make it the root of the BST
            pivot = len(cur_nums) // 2
            node = TreeNode(cur_nums[pivot])

            # Step 2: Recursively build the left subtree from the left half
            node.left = build_tree(cur_nums[:pivot])

            # Step 3: Recursively build the right subtree from the right half
            node.right = build_tree(cur_nums[pivot + 1 :])

            # Return the constructed node (root of this subtree)
            return node

        # Call the helper function with the entire list to start the recursion
        return build_tree(nums)


def main():
    """
    Main function to demonstrate the functionality of the Solution class.
    """

    # Create an instance of the Solution class
    solution = Solution()

    # Test case 1
    nums = [-10, -3, 0, 5, 9]
    result = solution.sortedArrayToBST(nums)
    # Check that the root is 0, left child is -3, and right child is 9
    assert result.val == 0
    assert result.left.val == -3
    assert result.right.val == 9

    # Test case 2
    nums = [1, 3]
    result = solution.sortedArrayToBST(nums)
    # Check that the root is 3 and left child is 1
    assert result.val == 3
    assert result.left.val == 1
    assert result.right is None

    # Test case 3
    nums = [1]
    result = solution.sortedArrayToBST(nums)
    # Check that the root is 1 and has no children
    assert result.val == 1
    assert result.left is None
    assert result.right is None

    print("All test cases passed!")


if __name__ == "__main__":
    main()
