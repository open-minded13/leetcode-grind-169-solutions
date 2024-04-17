from typing import Optional

# Date of Last Practice: Jan 21, 2024 -> Feb 29, 2024
#
# Time Complexity: O(K), where K is the input integer K.
#                  Once we've found the Kth smallest node, we can return its value immediately.
#                  However, when K equals the number of all nodes, K will be N.
#                  Therefore, O(K) in the best-case scenario (when K is much smaller than N) and
#                  O(N) in the worst-case scenario.
#
# Space Complexity: O(H), where H is the height of the tree.
#                   In a balanced tree, H will be log(N).
#                   In a skewed street, H will be N.
#                   Therefore, O(H) is in the best scenario,
#                   and O(N) is in the worst scenario.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        self.finder(root)
        return self.result

    def finder(self, node):
        if node == None:
            return
        self.finder(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self.finder(node.right)


class FirstSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            in_order.append(node)
            if node.right:
                dfs(node.right)

        dfs(root)
        return in_order[k - 1].val


# Test cases
def test():
    # Helper function to build a tree from a list
    def build_tree(lst, index=0):
        if index < len(lst) and lst[index] is not None:
            node = TreeNode(lst[index])
            node.left = build_tree(lst, 2 * index + 1)
            node.right = build_tree(lst, 2 * index + 2)
            return node
        return None

    sol = Solution()

    # Example 1
    tree1 = build_tree([3, 1, 4, None, 2])
    assert sol.kthSmallest(tree1, 1) == 1

    # Example 2
    tree2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert sol.kthSmallest(tree2, 3) == 3

    print("All tests passed.")


test()
