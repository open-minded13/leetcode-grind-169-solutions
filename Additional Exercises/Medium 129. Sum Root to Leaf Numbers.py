# Date of Last Practice: Mar 18, 2024
#
# Time Complexity: O(N), where N is the total number of nodes.
#                  We use depth-first search to traverse each node once.
#
# Space Complexity: O(H), where H is the height of the tree.
#                   This space is used by the call stack due to recursion.
#                   In the worst case, where the binary tree becomes a linked list (skewed tree),
#                   the height of the tree H can be N, making the worst-case space complexity O(N).
#                   However, for a balanced tree, the space complexity would be O(log N).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Initialize the total sum to 0
        self.sum = 0

        # Helper function to perform DFS traversal
        def _dfs(node, value_str):
            # If it's a leaf node, convert the accumulated string to int and add to sum
            if node.left is None and node.right is None:
                self.sum += int(value_str)
                return

            # Traverse left child if exists
            if node.left:
                _dfs(node.left, value_str + str(node.left.val))
            # Traverse right child if exists
            if node.right:
                _dfs(node.right, value_str + str(node.right.val))

        # Start DFS with root node
        _dfs(root, str(root.val))

        # Return the total sum
        return self.sum


class AntherSolution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0

        def _dfs(node, value):
            if node.left is None and node.right is None:
                self.sum += value
                return

            if node.left:
                _dfs(node.left, value * 10 + node.left.val)
            if node.right:
                _dfs(node.right, value * 10 + node.right.val)

        _dfs(root, root.val)

        return self.sum


# Helper function to create a binary tree from a list of values
def create_tree(values):
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Test cases
solution = Solution()
# Test case 1
root1 = create_tree([1, 2, 3])
assert solution.sumNumbers(root1) == 25, "Test case 1 failed"
# Test case 2
root2 = create_tree([4, 9, 0, 5, 1])
assert solution.sumNumbers(root2) == 1026, "Test case 2 failed"
# Additional test case 3 - more complex tree
root3 = create_tree([1, 2, 3, 4, 5, 6, 7])
assert solution.sumNumbers(root3) == 522, "Test case 3 failed"

print("All test cases passed!")
