# Date of Last Practice: Aug 31, 2023 -> Jan 25, 2024
#
# Time Complexity: O(N), where N is the total number of nodes in the tree.
#
# Space Complexity: O(H), where H is the height of the tree, due to the recursive call stack.
#                   In the worst case, the tree could be skewed, making the space complexity O(N).

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) >= 0

    def Height(self, root):
        if not root:
            return 0
        left_height, right_height = self.Height(root.left), self.Height(root.right)
        if (
            left_height == -1
            or right_height == -1
            or abs(right_height - left_height) > 1
        ):
            return -1
        else:
            return max(left_height, right_height) + 1


# Test cases
if __name__ == "__main__":
    # Create a balanced binary tree
    balanced_tree = TreeNode(1)
    balanced_tree.left = TreeNode(2)
    balanced_tree.right = TreeNode(3)
    balanced_tree.left.left = TreeNode(4)
    balanced_tree.left.right = TreeNode(5)
    balanced_tree.right.left = TreeNode(6)
    balanced_tree.right.right = TreeNode(7)

    # Create an unbalanced binary tree
    unbalanced_tree = TreeNode(1)
    unbalanced_tree.left = TreeNode(2)
    unbalanced_tree.left.left = TreeNode(3)

    solution = Solution()

    # Test case 1: The balanced_tree should return True
    assert solution.isBalanced(balanced_tree) == True

    # Test case 2: The unbalanced_tree should return False
    assert solution.isBalanced(unbalanced_tree) == False

    print("All test cases passed!")
