from typing import Optional, List
from collections import deque

# Date of Last Practice: Jan 4, 2024 -> Feb 21, 2024
#
# Time Complexity: O(N), where N is the number of nodes on the binary tree.
#                  We use a breadth-first search algorithm to traverse the binary tree
#                  level-by-level, and each node is visited once.
#
# Space Complexity: O(N), where N is the number of nodes on the binary tree.
#                   The maximum size of the queue is the maximum breadth of the tree,
#                   which could be n/2 in the worst case (a complete binary tree).
#                   So, the space complexity due to the queue is O(n).
#                   The output list stores the rightmost node of each level.
#                   In the worst case, this could be O(log n) for
#                   a balanced binary tree (height of the tree).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        output = []

        while queue:
            current_level_length = len(queue)
            for i in range(current_level_length):
                node = queue.popleft()
                if i == current_level_length - 1:
                    output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output


class First_Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        output = []

        while queue:
            current_level = deque()

            while queue:
                current_level.append(queue.popleft())

            is_right_sight = False
            while current_level:
                current_node = current_level.popleft()

                if current_node:
                    if not is_right_sight:
                        output.append(current_node.val)
                        is_right_sight = True
                    queue.append(current_node.right)
                    queue.append(current_node.left)

        return output


# Test Cases
def test_solution():
    # Case 1: Simple Binary Tree
    root1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert Solution().rightSideView(root1) == [1, 3, 4]

    # Case 2: Only right children
    root2 = TreeNode(1, None, TreeNode(3))
    assert Solution().rightSideView(root2) == [1, 3]

    # Case 3: Empty tree
    root3 = None
    assert Solution().rightSideView(root3) == []

    # Case 4: Complete Binary Tree
    root4 = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )
    assert Solution().rightSideView(root4) == [1, 3, 7]

    # Case 5: Skewed Tree (left)
    root5 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
    assert Solution().rightSideView(root5) == [1, 2, 3, 4, 5]

    # Case 6: Skewed Tree (right)
    root6 = TreeNode(
        1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5))))
    )
    assert Solution().rightSideView(root6) == [1, 2, 3, 4, 5]

    # Case 7: One node
    root7 = TreeNode(1)
    assert Solution().rightSideView(root7) == [1]

    # Case 8: Random tree
    root8 = TreeNode(
        10,
        TreeNode(2, TreeNode(4), TreeNode(16)),
        TreeNode(3, None, TreeNode(5, TreeNode(7), None)),
    )
    assert Solution().rightSideView(root8) == [10, 3, 5, 7]

    print("All test cases passed!")


test_solution()
