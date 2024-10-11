from typing import Optional

# Date of Last Practice: Jun 28, 2023 -> Jul 2, 2024
#
# Time Complexity: O(N), where N is the total number of nodes in the larger of
#                  the two input trees. In the worst case scenario, the method
#                  needs to visit all nodes of the larger tree to determine if
#                  they are the same.
#
# Space Complexity: O(H), where H is the height of the tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Test Cases
# Example 1:
#   Tree 1        Tree 2
#     1            1
#    / \          / \
#   2   3        2   3
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().isSameTree(p1, q1))  # Output: True

# Example 2:
#   Tree 1        Tree 2
#     1            1
#    /            /
#   2            2
p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print(Solution().isSameTree(p2, q2))  # Output: False

# Example 3:
#   Tree 1        Tree 2
#     1            1
#    / \          / \
#   2   1        1   2
p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
print(Solution().isSameTree(p3, q3))  # Output: False

# Additional Test Case:
# Both trees are empty
p4 = None
q4 = None
print(Solution().isSameTree(p4, q4))  # Output: True

# Additional Test Case:
# Tree 1 is empty, Tree 2 has one node with value 1
p5 = None
q5 = TreeNode(1)
print(Solution().isSameTree(p5, q5))  # Output: False
