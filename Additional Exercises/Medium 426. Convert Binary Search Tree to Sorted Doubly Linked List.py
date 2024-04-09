from typing import Optional

# Date of Last Practice: Mar 16, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the tree.
#
# Space Complexity: O(N), where N is the number of nodes in the tree.
#                   The space complexity consists of the space used by
#                   the recursion call stack during the inorder traversal.
#                   The height of a BST can be O(N) in the worst case
#                   (completely unbalanced tree) and O(log N) in the best case
#                   (completely balanced tree).


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        # Initialize the previous and head node references
        self.prev = None
        self.head = None

        # Step 1 - Perform inorder traversal to link nodes
        def _inorder_traversal(node):
            if not node:
                return

            _inorder_traversal(node.left)

            # For the first node, set it as the head
            if not self.prev:
                self.head = node
            else:
                # Link the current node with the previous one
                node.left = self.prev
                self.prev.right = node

            self.prev = node

            _inorder_traversal(node.right)

        _inorder_traversal(root)

        # Step 2 - Make the list circular
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head


class AnotherSolution:
    # This solution has a space complexity of O(N).
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        sorted_node = []

        def _inorder_traversal(node):
            if node is None:
                return
            _inorder_traversal(node.left)
            sorted_node.append(node)
            _inorder_traversal(node.right)

        _inorder_traversal(root)

        head = None
        pre_node = None
        for index, node in enumerate(sorted_node):
            if index == 0:
                head = node
                head.left = sorted_node[-1]
                head.right = (
                    sorted_node[index + 1] if index + 1 < len(sorted_node) else head
                )
                pre_node = head
            else:
                node.left = pre_node
                node.right = (
                    sorted_node[index + 1] if index + 1 < len(sorted_node) else head
                )
                pre_node = node

        return head


# Test cases
def test_solution():
    # Helper function to create a binary search tree from a list of values
    def create_bst_from_list(index, values):
        if index >= len(values) or values[index] is None:
            return None
        root = Node(values[index])
        root.left = create_bst_from_list(2 * index + 1, values)
        root.right = create_bst_from_list(2 * index + 2, values)
        return root

    # Helper function to validate the doubly linked list
    def validate_dll(head, expected_values):
        values = []
        current = head
        for _ in range(len(expected_values)):
            values.append(current.val)
            current = current.right
            if current == head:
                break
        assert values == expected_values, f"Expected {expected_values}, got {values}"

    sol = Solution()

    # Test case 1
    values1 = [4, 2, 5, 1, 3]
    bst1 = create_bst_from_list(0, values1)
    head1 = sol.treeToDoublyList(bst1)
    validate_dll(head1, [1, 2, 3, 4, 5])

    # Test case 2
    values2 = [2, 1, 3]
    bst2 = create_bst_from_list(0, values2)
    head2 = sol.treeToDoublyList(bst2)
    validate_dll(head2, [1, 2, 3])

    print("All test cases passed!")


test_solution()
