"""Provides functionality to serialize and deserialize binary trees.

This module defines a class that can convert a binary tree to and from a string
representation to allow it to be stored or transmitted more easily.
"""

from collections import deque

# Date of Last Practice: Apr 13, 2024 -> Oct 23, 2024
#
# Time Complexity: O(N), where N is the total number of nodes in the tree.
#                  We traverse each node exactly once. During the traversal,
#                  we perform a constant amount of work for each node, such
#                  as appending its value to the result list or adding its
#                  children to the queue. Thus, the time complexity is
#                  proportional to the number of nodes in the tree.
#
# Space Complexity: O(N), where N is the total number of nodes in the tree.
#
#                   Queue: At worst, the queue will hold all nodes at the widest
#                          level of the tree. This occurs when the tree is perfectly
#                          balanced or at its widest point, which could be up to 2/N
#                          nodes in a full binary tree.
#
#                   Result List: We also maintain a list to store the values of all
#                                nodes, which in the worst case will store N node
#                                values and N−1 null values for leaf nodes.


# Definition for a binary tree node.
class TreeNode:
    """A node in a binary tree.

    Attributes:
        val (int): The value stored in the node.
        left (TreeNode): A pointer to the left child of the node.
        right (TreeNode): A pointer to the right child of the node.
    """

    def __init__(self, x):
        """Initializes the TreeNode with a value and no children."""
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """Serializer and deserializer for binary trees using a BFS approach."""

    def serialize(self, root):
        """Converts a binary tree to a string.

        Args:
            root (TreeNode): The root of the binary tree to serialize.

        Returns:
            str: A string representation of the binary tree.
        """
        if not root:
            return ""

        bfs_queue = deque([root])
        result = []
        while bfs_queue:
            node = bfs_queue.popleft()  # O(1) time complexity
            if node:
                result.append(str(node.val))
                bfs_queue.append(node.left)
                bfs_queue.append(node.right)
            else:
                result.append("null")

        while result and result[-1] == "null":
            result.pop()

        return ",".join(result)

    def deserialize(self, data):
        """Reconstructs a binary tree from a string.

        Args:
            data (str): The string representation of the binary tree.

        Returns:
            TreeNode: The root of the reconstructed binary tree.
        """
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        bfs_queue = deque([root])
        index = 1
        while bfs_queue:
            node = bfs_queue.popleft()  # O(1) time complexity
            if index < len(values) and values[index] != "null":
                node.left = TreeNode(int(values[index]))
                bfs_queue.append(node.left)
            index += 1
            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                bfs_queue.append(node.right)
            index += 1

        return root


def main():
    """Demonstrates the serialization and deserialization of a binary tree."""
    ser = Codec()
    deser = Codec()

    # Example tree: [1,2,3,null,null,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    serialized = ser.serialize(root)
    print(f"Serialized tree: {serialized}")
    deserialized = deser.deserialize(serialized)
    assert ser.serialize(deserialized) == serialized


if __name__ == "__main__":
    main()
