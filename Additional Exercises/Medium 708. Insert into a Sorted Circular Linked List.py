# Date of Last Practice: Mar 17, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the circular linked list.
#                  In the worst-case scenario, it loops through all the nodes
#                  if the correct insertion point is at the end of the list
#                  or if it needs to identify the maximum or minimum elements
#                  in a fully sorted list.
#
# Space Complexity: O(1). The solution creates a single new node regardless of
#                   the input size and does not use any additional data structures
#                   that grow with the input size.


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        new_node = Node(insertVal)
        if not head:
            # Step 1 - Handle empty list
            new_node.next = new_node
            return new_node
        elif head.next is head:
            # Step 2 - Handle list with a single node
            head.next = new_node
            new_node.next = head
            return head

        cur_node, pre_node = head.next, head
        while True:
            if cur_node.val >= insertVal >= pre_node.val:
                # Step 3 - Regular insert between two nodes
                pre_node.next = new_node
                new_node.next = cur_node
                break
            elif cur_node.val < pre_node.val or cur_node is head:
                # Step 4 - Handle insert at the list's min or max point (wrap-around)
                if insertVal < cur_node.val or insertVal > pre_node.val:
                    pre_node.next = new_node
                    new_node.next = cur_node
                    break
            pre_node = cur_node
            cur_node = cur_node.next
        return head


# Helper function to convert list to circular linked list and vice versa
def list_to_circular_linked_list(lst, insertVal):
    head = None
    tail = None
    for val in lst:
        new_node = Node(val)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    if tail:
        tail.next = head  # Make it circular
    solution = Solution()
    return solution.insert(head, insertVal)


def circular_linked_list_to_list(head):
    if not head:
        return []
    lst = [head.val]
    node = head.next
    while node != head:
        lst.append(node.val)
        node = node.next
    return lst


# Test cases
assert circular_linked_list_to_list(list_to_circular_linked_list([3, 4, 1], 2)) == [
    3,
    4,
    1,
    2,
]
assert circular_linked_list_to_list(list_to_circular_linked_list([], 1)) == [1]
assert circular_linked_list_to_list(list_to_circular_linked_list([1], 0)) == [1, 0]

print("All test cases passed.")
