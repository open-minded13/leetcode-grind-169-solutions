# Date of Last Practice: Jul 01, 2023 -> Feb 1, 2024
#
# Time Complexity: O(N), where N is the total number of nodes in the given tree.
#                  This is because the solution recursively visits each node
#                  in the tree exactly once.
#
# Space Complexity: O(H), where H is the height of the tree. In the recursive calls,
#                   the maximum depth of the call stack is equal to the height of the tree.
#                   Therefore, the space complexity is determined by the maximum depth of
#                   the recursion, which is the height of the tree.
#                   In the worst case, for a skewed tree, the height can be equal to
#                   the number of nodes N, resulting in a space complexity of O(N).
#                   However, for a balanced tree, the height is logarithmic in the number of nodes,
#                   resulting in a space complexity of O(log N).
#                   So, the space complexity is O(H) or O(log N),
#                   depending on the height of the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Test cases
# Test case 1: Empty tree
# Expected output: 0
tree1 = None
solution = Solution()
print(solution.maxDepth(tree1))

# Test case 2: Single node tree
# Expected output: 1
tree2 = TreeNode(1)
solution = Solution()
print(solution.maxDepth(tree2))

# Test case 3: Full binary tree
# Expected output: 3
tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.right = TreeNode(3)
tree3.left.left = TreeNode(4)
tree3.left.right = TreeNode(5)
tree3.right.left = TreeNode(6)
tree3.right.right = TreeNode(7)
solution = Solution()
print(solution.maxDepth(tree3))

# Test case 4: Tree with only left child
# Expected output: 4
tree4 = TreeNode(1)
tree4.left = TreeNode(2)
tree4.left.left = TreeNode(3)
tree4.left.left.left = TreeNode(4)
solution = Solution()
print(solution.maxDepth(tree4))

# Test case 5: Tree with only right child
# Expected output: 4
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.right = TreeNode(3)
tree5.right.right.right = TreeNode(4)
solution = Solution()
print(solution.maxDepth(tree5))
