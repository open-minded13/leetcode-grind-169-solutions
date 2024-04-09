# Date of Last Practice: Jul 1 2023


class TreeNode:
    # Step 1: Create a Tree Node Class
    #         We'll start by creating a class to represent a node in the tree.
    #         Each node will have a value and a list of child nodes.
    def __init__(self, value):
        self.value = value
        self.children = []

    # Step 2: Implement Tree Operations
    #         Next, let's define some common operations you can perform on a tree:
    def add_child(self, child_node):
        self.children.append(child_node)

    def depth_first_traversal(self):
        print(self.value)
        for child in self.children:
            child.depth_first_traversal()

    def breadth_first_traversal(self):
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.value)
            queue.extend(node.children)

    def count_nodes(self):
        count = 1
        for child in self.children:
            count += child.count_nodes()
        return count

    def tree_height(self):
        # In Python, when a list is empty, it is not equal to None.
        # Instead, you should check if the list is empty by using if not node.children.
        if not self.children:
            return 0
        return 1 + max(child.tree_height() for child in self.children)

    # def tree_height(self):
    #     if not self.children:
    #         return 0
    #     height = 1
    #     max_height = 1
    #     for child in self.children:
    #         height = height + child.tree_height()
    #         max_height = max(max_height, height)
    #         height = 1
    #     return max_height

    # Convert a tree into a string representation (serialization).
    def serialization_of_tree(self):
        if not self:
            return ""
        serialized_list = [self.value]
        for child in self.children:
            serialized_list.append(child.serialization_of_tree())
        separator = ","
        return separator.join(serialized_list)

    # Reconstruct a tree from its string representation (deserialization).
    # NOTE: The new tree structure may not be the same as the original tree.
    def deserialize_tree(self, serialization):
        if not serialization:
            return None
        serialized_list = serialization.split(",")
        self.value = serialized_list[0]
        for item in serialized_list[1:]:
            child = TreeNode(None)
            child.deserialize_tree(item)
            self.add_child(child)
        return self

    def tree_search(self, target):
        if self.value == target:
            return self
        for child in self.children:
            result = child.tree_search(target)
            if result:
                return result
        return None


# Create nodes
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

# Build the tree
root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)

# Traverse the tree
print("Depth-First Traversal:")
root.depth_first_traversal()

print("Breadth-First Traversal:")
root.breadth_first_traversal()

# Count nodes
print("Number of Nodes:", root.count_nodes())

# Get the tree height/depth
print("Tree Height:", root.tree_height())

# Convert the tree into a string
serialization = root.serialization_of_tree()
print("Serialized Tree:", serialization)

# Convert a string back to a tree (but the structure may not be the same as the original tree)
new_root = TreeNode(None)
new_root.deserialize_tree(serialization)
print("Deserialized Tree:")
new_root.depth_first_traversal()
print("Tree Height of the Deserialized Tree:", new_root.tree_height())

search_result = root.tree_search("E")
if search_result:
    print("Found:", search_result.value)
else:
    print("Not found")
