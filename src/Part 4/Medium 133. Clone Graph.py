from typing import Optional
from collections import deque

# Date of Last Practice: Nov 19, 2023 -> Feb 4, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the graph.
#                  If the graph is connected with no repeated edges and no self-loops,
#                  and all nodes can be visited starting from the given node,
#                  then each edge is traversed twice during the process of cloning the graph.
#                  Since there are N-1 edges in the graph, O(2*(N-1)) ≈ O(N).
#
# Space Complexity: O(N), where N is the number of nodes in the graph.
#                   This is because we use the node_mapping dictionary to store each cloned node.


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        # Dictionary to store the mapping of original nodes to their clones
        node_mapping = {}

        # Create the first node and add it to the mapping
        cloned_node = Node(node.val)
        node_mapping[node] = cloned_node

        # Queue for BFS traversal
        queue = deque([node])

        # Perform BFS
        while queue:
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:
                if neighbor not in node_mapping:
                    # If the neighbor is not in the mapping, create a clone
                    cloned_neighbor = Node(neighbor.val)
                    node_mapping[neighbor] = cloned_neighbor
                    queue.append(neighbor)

                # Add the cloned neighbor to the cloned_node's neighbors
                node_mapping[current_node].neighbors.append(node_mapping[neighbor])

        return cloned_node


# Test cases
def test_clone_graph():
    # Example 1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloned_node1 = solution.cloneGraph(node1)

    # Check if the cloned graph is correct
    assert cloned_node1.val == node1.val
    assert cloned_node1.neighbors[0].val == node2.val
    assert cloned_node1.neighbors[1].val == node4.val

    # Example 2
    node1 = Node(1)
    solution = Solution()
    cloned_node1 = solution.cloneGraph(node1)

    # Check if the cloned graph is correct
    assert cloned_node1.val == node1.val
    assert not cloned_node1.neighbors  # No neighbors

    print("All test cases passed!")


# Run the test cases
test_clone_graph()
