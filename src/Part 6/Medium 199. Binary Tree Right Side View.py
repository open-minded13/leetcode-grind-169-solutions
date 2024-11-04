"""Binary Tree Right Side View solution.

This module includes two solutions to the problem of finding the right-side 
view of a binary tree. The FirstSolution class contains an initial approach 
for comparison, while the Solution class provides an optimized version. The 
improvement is explained within the comments for easy reference.

Typical usage example:

  # Build the tree
  root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))

  # Get the right side view
  result = Solution().rightSideView(root)  # Output: [1, 3, 4]
"""

from typing import Optional, List
from collections import deque

# Date of Last Practice: Jan 4, 2024 -> Feb 21, 2024 -> Nov 3, 2024
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
    """Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node.
        left (TreeNode, optional): The left child node.
        right (TreeNode, optional): The right child node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Optimized solution to find the right-side view of a binary tree.

    This solution uses only one queue to store nodes level-by-level. It
    collects the last node of each level, which corresponds to the visible
    node from the right side.
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        output = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                # Step 1 - Check if node is last in level (rightmost)
                if i == level_length - 1:
                    output.append(node.val)

                # Step 2 - Add children to the queue (left, then right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output


class FirstSolution:
    """Initial solution to find the right-side view of a binary tree.

    This solution is inefficient because it uses two deques per level,
    which increases memory usage. It also unnecessarily traverses nodes
    from left to right, adding left children to the queue first,
    which is unnecessary for right-side view.
    """

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


def test_solution():
    """Runs test cases to verify the solutions."""

    # Test Case 1: Simple Binary Tree
    root1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert Solution().rightSideView(root1) == [1, 3, 4]
    assert FirstSolution().rightSideView(root1) == [1, 3, 4]

    # Test Case 2: Only right children
    root2 = TreeNode(1, None, TreeNode(3))
    assert Solution().rightSideView(root2) == [1, 3]
    assert FirstSolution().rightSideView(root2) == [1, 3]

    # Test Case 3: Empty tree
    root3 = None
    assert not Solution().rightSideView(root3)
    assert not FirstSolution().rightSideView(root3)

    # Test Case 4: Complete Binary Tree
    root4 = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )
    assert Solution().rightSideView(root4) == [1, 3, 7]
    assert FirstSolution().rightSideView(root4) == [1, 3, 7]

    # Test Case 5: Skewed Tree (left)
    root5 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
    assert Solution().rightSideView(root5) == [1, 2, 3, 4, 5]
    assert FirstSolution().rightSideView(root5) == [1, 2, 3, 4, 5]

    # Test Case 6: Skewed Tree (right)
    root6 = TreeNode(
        1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5))))
    )
    assert Solution().rightSideView(root6) == [1, 2, 3, 4, 5]
    assert FirstSolution().rightSideView(root6) == [1, 2, 3, 4, 5]

    # Test Case 7: One node
    root7 = TreeNode(1)
    assert Solution().rightSideView(root7) == [1]
    assert FirstSolution().rightSideView(root7) == [1]

    # Test Case 8: Random tree
    root8 = TreeNode(
        10,
        TreeNode(2, TreeNode(4), TreeNode(16)),
        TreeNode(3, None, TreeNode(5, TreeNode(7), None)),
    )
    assert Solution().rightSideView(root8) == [10, 3, 5, 7]
    assert FirstSolution().rightSideView(root8) == [10, 3, 5, 7]

    print("All test cases passed for both solutions.")


if __name__ == "__main__":
    test_solution()
