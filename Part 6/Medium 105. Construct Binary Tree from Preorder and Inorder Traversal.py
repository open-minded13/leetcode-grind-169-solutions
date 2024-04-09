from typing import List, Optional

# Date of Last Practice: Jan 1, 2024 -> Feb 20, 2024
#
# Time Complexity: O(N), where N is the number of nodes.
#                  Creating the hashmap (inorder_index_map) takes O(N) time.
#                  The find_subtree function is called once for each node in the tree.
#                  For each call, the operations performed
#                  (like looking up in the hashmap and creating a new TreeNode) take O(1) time.
#                  Therefore, the overall time complexity is O(N).
#
# Space Complexity: O(N), where N is the number of nodes.
#                   The space complexity for the hashmap is O(N).
#                   The space complexity of the recursion stack is O(H),
#                   where H is the height of the tree.
#                   In the worst case (a skewed tree), h can be O(N),
#                   but in a balanced tree, it would be O(log N).
#                   Overall, The space complexity is dominated by building hashmap, O(N).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {inorder[i]: i for i in range(len(inorder))}

        def find_subtree(left, right):
            if left > right:
                return None

            # NOTE: pop(0) != pop()
            root_value = preorder.pop(0)
            root = TreeNode(root_value)
            position = inorder_index_map[root_value]

            root.left = find_subtree(left, position - 1)
            root.right = find_subtree(position + 1, right)

            return root

        return find_subtree(0, len(inorder) - 


# Helper function to get the inorder traversal of the tree
def get_inorder(node):
    return get_inorder(node.left) + [node.val] + get_inorder(node.right) if node else []


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
