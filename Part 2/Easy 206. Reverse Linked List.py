# Date of Last Practice: Jun 19, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#                  This is because the method iterates through each node once in the while loop,
#                  performing constant-time operations for each node.
#
# Space Complexity: O(1). This is because it uses a constant amount of additional space.
#                   The method only utilizes a few variables (current, previous, next_node),
#                   regardless of the size of the input linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        head = previous
        return head


# Test Cases
# Case 1: Empty List
# Expected Output: None
list1 = None
sol = Solution()
reversed_list1 = sol.reverseList(list1)
print(reversed_list1)

# Case 2: Single Node List
# Expected Output: ListNode(1)
list2 = ListNode(1)
sol = Solution()
reversed_list2 = sol.reverseList(list2)
print(reversed_list2.val)

# Case 3: List with multiple nodes
# Expected Output: 5 -> 4 -> 3 -> 2 -> 1
list3 = ListNode(1)
list3.next = ListNode(2)
list3.next.next = ListNode(3)
list3.next.next.next = ListNode(4)
list3.next.next.next.next = ListNode(5)
sol = Solution()
reversed_list3 = sol.reverseList(list3)
current = reversed_list3
while current is not None:
    print(current.val, "->", end=" ")
    current = current.next
