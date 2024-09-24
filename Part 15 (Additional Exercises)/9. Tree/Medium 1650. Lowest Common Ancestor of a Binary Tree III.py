# Date of Last Practice: Mar 10, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the tree.
#                  In the worst case, especially in a skewed tree,
#                  the complexity would be O(H) for each traversal,
#                  where H is the height of the tree.
#                  Since the algorithm does two upward traversals
#                  (first from p to q and then from q to p),
#                  the worst-case time complexity is O(2H), which simplifies to O(H).
#
#                  Given that the height of the tree can, in the worst case,
#                  be proportional to the number of nodes (N) in a skewed binary tree,
#                  the time complexity in such scenarios is O(N).
#
# Space Complexity: O(N), where N is the number of nodes in the tree.
#                   In the worst case, the visited_ancestors and
#                   the recursive call stack will be O(H),
#                   where H could be N in a skewed tree.


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        self.lowest_common_ancestor = None
        self.visited_ancestors = set()

        def _upward_tracking(node, target):
            if node is None:
                return
            if self.lowest_common_ancestor is None and (
                node in self.visited_ancestors or node == target
            ):
                self.lowest_common_ancestor = node
                return
            self.visited_ancestors.add(node)
            _upward_tracking(node.parent, target)

        _upward_tracking(p, q)  # Step 1 - Track upwards from p, marking visited nodes.
        _upward_tracking(
            q, p
        )  # Step 2 - Track upwards from q to find the common ancestor.
        return self.lowest_common_ancestor


# Helper function to link nodes (simplifying test case setup).
def link_nodes(parent, left=None, right=None):
    parent.left = left
    parent.right = right
    if left:
        left.parent = parent
    if right:
        right.parent = parent


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    node3 = Node(3)
    node5 = Node(5)
    node1 = Node(1)
    node6 = Node(6)
    node2 = Node(2)
    node0 = Node(0)
    node8 = Node(8)
    node7 = Node(7)
    node4 = Node(4)
    link_nodes(node3, node5, node1)
    link_nodes(node5, node6, node2)
    link_nodes(node1, node0, node8)
    link_nodes(node2, node7, node4)
    assert sol.lowestCommonAncestor(node5, node1).val == 3, "Test case 1 failed"

    # Test case 2
    assert sol.lowestCommonAncestor(node5, node4).val == 5, "Test case 2 failed"

    # Test case 3
    node1 = Node(1)
    node2 = Node(2)
    link_nodes(node1, None, node2)
    assert sol.lowestCommonAncestor(node1, node2).val == 1, "Test case 3 failed"

    print("All test cases passed.")
