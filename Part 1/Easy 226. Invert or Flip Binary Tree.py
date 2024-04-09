# # Date of Last Practice: Jul 01, 2023 -> Jan 29, 2024
#
# Time Complexity: O(N), where N is the total number of nodes in the given tree.
#                  This is because the solution recursively visits each node in the tree exactly once.
#
# Space Complexity: O(H), where H is the height of the tree. In the recursive calls,
#                   the maximum depth of the call stack is equal to the height of the tree.
#                   Therefore, the space complexity is determined by the maximum depth of the recursion,
#                   which is the height of the tree.
#                   In the worst case, for a skewed tree, the height can be equal to the number of nodes N,
#                   resulting in a space complexity of O(N).
#                   However, for a balanced tree, the height is logarithmic in the number of nodes,
#                   resulting in a space complexity of O(log N).
#                   So, the space complexity is O(H) or O(log N), depending on the height of the tree.

# NOTE: Call Stack: When a function is called recursively,
#                   the system allocates memory on the call stack to store the function call,
#                   including its parameters, return address, and local variables.
#                   The call stack grows as new function calls are made and shrinks as the function calls return.


# Definition for a binary tree node.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # Adding the following judgments can reduce memory usage.
        if not root.left and not root.right:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        # Python provides a neat way to swap the values of two variables in order to perform the following operations.
        # node = TreeNode()
        # node = root.left
        # root.left = root.right
        # root.right = node
        root.left, root.right = root.right, root.left
        return root


# Test Cases
# Test Case 1: Inverting a tree with single node
# Input:
#     1
# Output:
#     1
test_case_1 = TreeNode(1)
inverted_tree_1 = Solution().invertTree(test_case_1)
print(inverted_tree_1.val)  # Expected output: 1
print(inverted_tree_1.left)  # Expected output: None
print(inverted_tree_1.right)  # Expected output: None

# Test Case 2: Inverting a tree with three nodes
# Input:
#      4
#     / \
#    2   7
# Output:
#      4
#     / \
#    7   2
test_case_2 = TreeNode(4)
test_case_2.left = TreeNode(2)
test_case_2.right = TreeNode(7)
inverted_tree_2 = Solution().invertTree(test_case_2)
print(inverted_tree_2.val)  # Expected output: 4
print(inverted_tree_2.left.val)  # Expected output: 7
print(inverted_tree_2.right.val)  # Expected output: 2

# Test Case 3: Inverting a tree with multiple levels
# Input:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
# Output:
#         1
#        / \
#       3   2
#      /   / \
#     6   5   4
test_case_3 = TreeNode(1)
test_case_3.left = TreeNode(2)
test_case_3.right = TreeNode(3)
test_case_3.left.left = TreeNode(4)
test_case_3.left.right = TreeNode(5)
test_case_3.right.right = TreeNode(6)
inverted_tree_3 = Solution().invertTree(test_case_3)
print(inverted_tree_3.val)  # Expected output: 1
print(inverted_tree_3.left.val)  # Expected output: 3
print(inverted_tree_3.right.val)  # Expected output: 2
print(inverted_tree_3.left.left.val)  # Expected output: 6
print(inverted_tree_3.right.left.val)  # Expected output: 5
print(inverted_tree_3.right.right.val)  # Expected output: 4
