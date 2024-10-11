from typing import Optional

# Date of Last Practice: Mar 4, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#
#                  Copying the linked list (excluding random pointers):
#                  During this iteration, it creates a new copy of each node
#                  and stores it in a hash map (visited_node_dict)
#                  with the original node as the key.
#
#                  Copying the random pointers:
#                  After copying the nodes, the solution iterates over the list again
#                  to copy the random pointers.
#
# Space Complexity: O(N), where N is the number of nodes in the linked list.
#                   This hash map stores a mapping from the original nodes to the copied nodes.
#                   The space for the newly created nodes is also O(n),
#                   but this is considered the space required for the output
#                   rather than the auxiliary space used by the algorithm.


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Initialize variables
        visited_node_dict = {}
        current_node = head

        # Copy the linked list
        prev_node = None
        while current_node:
            if current_node not in visited_node_dict:
                node = Node(current_node.val)
                visited_node_dict[current_node] = node
                if prev_node:
                    prev_node.next = node
            prev_node = node
            current_node = current_node.next

        # Copy the random pointers
        current_node = head
        while current_node:
            current_new_node = visited_node_dict[current_node]
            current_new_node.random = visited_node_dict.get(current_node.random, None)
            current_node = current_node.next

        return visited_node_dict[head]


class ElegantSolution:
    # This solution reduces the auxiliary space complexity to O(1) as it doesn't use a hash map.

    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None

        # Step 1: Create interleaved list of original and copied nodes
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        # Step 2: Copy random pointers
        current = head
        while current:
            current.next.random = current.random.next if current.random else None
            current = current.next.next

        # Step 3: Separate the interleaved lists
        current_original = head
        current_copy = head.next
        copy_head = head.next
        while current_original:
            current_original.next = current_original.next.next
            current_copy.next = current_copy.next.next if current_copy.next else None
            current_original = current_original.next
            current_copy = current_copy.next

        return copy_head


# Helper functions to build and verify linked lists
def build_list(nodes):
    if not nodes:
        return None
    node_list = [Node(x) for x, _ in nodes]
    for i, (_, random_index) in enumerate(nodes):
        if random_index is not None:
            node_list[i].random = node_list[random_index]
    for i in range(1, len(node_list)):
        node_list[i - 1].next = node_list[i]
    return node_list[0]


def extract_list(head):
    result = []
    current = head
    nodes = []
    while current:
        nodes.append(current)
        current = current.next
    for node in nodes:
        if node.random is not None:
            index = nodes.index(node.random)
        else:
            index = None
        result.append([node.val, index])
    return result


# Test cases
sol = Solution()

# Test case 1
nodes1 = build_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
copied1 = sol.copyRandomList(nodes1)
assert extract_list(copied1) == [
    [7, None],
    [13, 0],
    [11, 4],
    [10, 2],
    [1, 0],
], "Test case 1 failed"

# Test case 2
nodes2 = build_list([[1, 1], [2, 1]])
copied2 = sol.copyRandomList(nodes2)
assert extract_list(copied2) == [[1, 1], [2, 1]], "Test case 2 failed"

# Test case 3
nodes3 = build_list([[3, None], [3, 0], [3, None]])
copied3 = sol.copyRandomList(nodes3)
assert extract_list(copied3) == [[3, None], [3, 0], [3, None]], "Test case 3 failed"

print("All test cases passed successfully.")
