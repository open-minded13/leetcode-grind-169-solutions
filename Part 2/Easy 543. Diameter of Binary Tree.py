from typing import Optional

# Date of Last Practice: Nov 6, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
#                  The reason is that we traverse each node once.
#
# Space Complexity: O(H), where H is the height of the binary tree.
#                   In the worst case, if the tree is completely unbalanced,
#                   H can be equal to N (the number of nodes),
#                   but in a balanced tree, the height is typically much smaller.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # In Python, when you modify an element of a mutable object (such as a list) within a function,
    # the changes are reflected outside the function as well.
    # So, when we modify diameter[0] inside the dfs_counter function,
    # it is effectively modifying the same list that is accessible
    # in the diameterOfBinaryTree function.
    #
    # Mutable objects in Python include lists, dictionaries, and sets.

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs_counter(root):
            if root is None:
                return 0
            left_max_depth_of_node = dfs_counter(root.left)
            right_max_depth_of_node = dfs_counter(root.right)
            diameter[0] = max(
                diameter[0], left_max_depth_of_node + right_max_depth_of_node
            )
            return max(left_max_depth_of_node, right_max_depth_of_node) + 1

        # You can think of diameter[0] as a shared variable
        # between the diameterOfBinaryTree and dfs_counter functions,
        # allowing them to communicate and update the maximum diameter
        # across recursive calls without the need to pass it explicitly as a function argument.
        diameter = [0]

        # You do not have to pass diameter into the function as it is a mutable object.
        dfs_counter(root)

        return diameter[0]


class First_Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return 0

        def dfs_counter(root, diameter, node_max_length):
            if root.left == None and root.right == None:
                return 1, 1

            left_max_length, right_max_length, left_diameter, right_diameter = (
                0,
                0,
                0,
                0,
            )
            if root.left != None:
                left_max_length, left_diameter = dfs_counter(
                    root.left, diameter, node_max_length
                )
            if root.right != None:
                right_max_length, right_diameter = dfs_counter(
                    root.right, diameter, node_max_length
                )
            diameter = max(
                left_diameter, right_diameter, left_max_length + right_max_length
            )
            return max(left_max_length, right_max_length) + 1, diameter

        _, diameter = dfs_counter(root, diameter=0, node_max_length=0)

        return diameter


# Test cases
if __name__ == "__main__":
    s = Solution()

    # Create the following tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    assert s.diameterOfBinaryTree(root) == 3  # Diameter is the path 4 -> 2 -> 1 -> 3

    # Create a single-node tree
    root = TreeNode(1)
    assert s.diameterOfBinaryTree(root) == 0  # Diameter of a single-node tree is 0

    # Create a tree with only left subtrees
    #     1
    #    /
    #   2
    #  /
    # 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert s.diameterOfBinaryTree(root) == 2  # Diameter is the path 3 -> 2 -> 1

    # Create a tree with only right subtrees
    #   1
    #    \
    #     2
    #      \
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert s.diameterOfBinaryTree(root) == 2  # Diameter is the path 1 -> 2 -> 3

    print("All test cases passed!")
