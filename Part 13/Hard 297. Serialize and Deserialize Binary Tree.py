from collections import deque

# Date of Last Practice: Apr 13, 2024
#
# Time Complexity: O(N), where N is the total number of nodes in the tree.
#                  We traverse each node exactly once. During the traversal,
#                  we perform a constant amount of work for each node,
#                  such as appending its value to the result list or
#                  adding its children to the queue.
#                  Thus, the time complexity is proportional to the number of nodes in the tree.
#
# Space Complexity: O(N), where N is the total number of nodes in the tree.
#
#                   Queue: At worst, the queue will hold all nodes at the widest level of the tree.
#                          This occurs when the tree is perfectly balanced or at its widest point,
#                          which could be up to 2/N nodes in a full binary tree.
#
#                   Result List: We also maintain a list to store the values of all nodes,
#                                which in the worst case will store N node values and
#                                N−1 null values for leaf nodes.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        values = data.split(",")
        index = 1
        root = TreeNode(int(values[0]))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if index < len(values) and values[index] != "null":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
# Test cases
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(5)

# Testing serialization and deserialization
data = ser.serialize(root1)
assert data == "1,2,3,null,null,4,5,null,null,null,null"
assert (
    ser.serialize(deser.deserialize(data)) == "1,2,3,null,null,4,5,null,null,null,null"
)

# Test empty tree
data = ser.serialize(None)
assert data == ""
assert ser.serialize(deser.deserialize(data)) == ""

print("All test cases passed!")
