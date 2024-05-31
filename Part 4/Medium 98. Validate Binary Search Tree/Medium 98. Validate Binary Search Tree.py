import sys

# Date of Last Practice: Dec 12, 2023 -> Feb 7, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the tree.
#                  The algorithm performs a depth-first traversal of the binary tree.
#                  During this traversal, it visits every node exactly once.
#
# Space Complexity: O(N), where N is the number of nodes in the tree.
#                   For a skewed tree (worst case), the space complexity is O(N).
#                   For a balanced tree, the space complexity is O(log N).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(root, min_value, max_value):
            if root is None:
                return True
            if root.val <= min_value or root.val >= max_value:
                return False
            is_valid_left = isValid(root.left, min_value, root.val)
            is_valid_right = isValid(root.right, root.val, max_value)
            return is_valid_left and is_valid_right

        return isValid(root, -sys.maxsize - 1, sys.maxsize)


# Helper function to build a tree from a list
def buildTree(nodes, index=0):
    if index < len(nodes) and nodes[index] is not None:
        node = TreeNode(nodes[index])
        node.left = buildTree(nodes, 2 * index + 1)
        node.right = buildTree(nodes, 2 * index + 2)
        return node
    return None


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: The tree [2,1,3] is a valid BST.
    tree1 = buildTree([2, 1, 3])
    assert sol.isValidBST(tree1) == True

    # Test case 2: The tree [5,1,4,None,None,3,6] is not a valid BST.
    tree2 = buildTree([5, 1, 4, None, None, 3, 6])
    assert sol.isValidBST(tree2) == False

    print("All test cases passed!")
