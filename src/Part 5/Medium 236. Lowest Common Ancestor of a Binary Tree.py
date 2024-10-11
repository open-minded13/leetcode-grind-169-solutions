# Date of Last Practice: Dec 26, 2023 -> Feb 13, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the tree.
#                  The DFS algorithm traverses each node of the binary tree once
#                  to determine the LCA. Regardless of the tree's structure
#                  (whether balanced or skewed), in the worst-case scenario,
#                  the algorithm might need to visit all the nodes to find p and q.
#                  This is especially true if p and q are located at the leaf nodes
#                  farthest from the root.
#
# Space Complexity: O(H), where H is the maximum depth of the tree.
#                   In a balanced binary tree, the height is approximately log(N),
#                   leading to a space complexity of O(H) = O(log(N)).
#                   However, in a skewed tree (which resembles a linear structure),
#                   the height becomes proportional to N,
#                   and thus the space complexity also becomes O(H) = O(N).
#
# Note: Why using unlocal in another solution? In Python, if a list (or any mutable object)
#       is defined in an outer scope, you can access and modify its contents directly in
#       an inner function without declaring it as nonlocal. This behavior applies to operations that
#       modify the contents of the list, such as append(), remove(), or change an element by index.
#       However, in your code, you are not just modifying the contents of
#       p_ancestors and q_ancestors within the dfs function;
#       you are assigning new lists to these variables.
#       This assignment operation is what makes them local to the dfs function
#       unless specified otherwise using nonlocal.
#
# Note: `global` is used to declare variables that are defined at the top level
#       of the script or module, outside of all functions.
#       These are variables that are not inside any function and
#       are intended to be used throughout the entire module or script.
#
# Note: `nonlocal``, on the other hand, is used to refer to variables that are defined
#       in the nearest enclosing scope that is not the global scope.
#       This means that nonlocal is used for variables that are not global
#       but are also not local to the current function.


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None or root is p or root is q:
            return root

        left_is_found = self.lowestCommonAncestor(root.left, p, q)
        right_is_found = self.lowestCommonAncestor(root.right, p, q)

        if left_is_found and right_is_found:
            return root

        return left_is_found if left_is_found else right_is_found


# This solution has the same time and space complexity but uses more extra lists
# (search_path, p_ancestors, q_ancestors) that can be eliminated.
class Another_Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node, p, q):
            nonlocal p_ancestors, q_ancestors
            if node is None:
                return
            if node.val == p.val:
                search_path.append(node)
                p_ancestors = search_path.copy()
                if q_ancestors:
                    return
            elif node.val == q.val:
                search_path.append(node)
                q_ancestors = search_path.copy()
                if p_ancestors:
                    return
            else:
                search_path.append(node)

            dfs(node.left, p, q)
            dfs(node.right, p, q)
            search_path.pop()

        search_path = []
        p_ancestors = []
        q_ancestors = []
        dfs(root, p, q)

        ancestors_set = set(q_ancestors)
        for ancestor in reversed(p_ancestors):
            if ancestor in ancestors_set:
                return ancestor


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Helper function to create a tree from a list
def create_tree(lst, index=0):
    if index < len(lst) and lst[index] is not None:
        node = TreeNode(lst[index])
        node.left = create_tree(lst, 2 * index + 1)
        node.right = create_tree(lst, 2 * index + 2)
        return node
    return None


sol = Solution()

# Test Case 1: Basic Case
tree1 = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(sol.lowestCommonAncestor(tree1, tree1.left, tree1.right).val)  # Should return 3

# Test Case 2: LCA as One of the Nodes
tree2 = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(
    sol.lowestCommonAncestor(tree2, tree2.left, tree2.left.right.right).val
)  # Should return 5

# Test Case 3: Skewed Tree
tree3 = create_tree([1, 2, None, 3])
print(
    sol.lowestCommonAncestor(tree3, tree3.left, tree3.left.left).val
)  # Should return 2

# Test Case 4: Large Tree
tree4 = create_tree([i for i in range(1, 16)])  # A complete binary tree with 15 nodes
print(
    sol.lowestCommonAncestor(tree4, tree4.left.left, tree4.right.right).val
)  # Should return 1
