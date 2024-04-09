from typing import Optional

# Date of Last Practice: Nov 6, 2023 -> Feb 2, 2024
#
# Time Complexity: O(N), where N is the number of elements in the linked list.
#
# Space Complexity: O(1), because we only use two pointers, slow_pointer and fast_pointer,
#                   regardless of the size of the linked list. These pointers use a constant amount of space.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Two-Pointers Technique is really useful:
    #
    # 1) Middle of a Linked List:
    #    The two-pointer method is used to find the middle of a linked list.
    #    One pointer (slow_pointer) advances one node at a time,
    #    while the other pointer (fast_pointer) advances two nodes at a time.
    #    When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
    #
    # 2) Floyd's Cycle Finding Algorithm (Easy 141. Linked List Cycle):
    #    This algorithm is used to detect the presence of a cycle in a linked list.
    #    It also uses two pointers — one slow and one fast.
    #    If there's a cycle, the fast pointer will eventually catch up to
    #    the slow pointer as they move through the list.

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer


class First_Solution:
    # Time Complexity: O(N), where N is the number of elements in the linked list.
    #
    # Space Complexity: O(N), because the stack used to store the nodes of the linked list requires O(n) space.
    #
    # While this solution works, it uses additional space for the stack, which is not necessary.
    # There is a more efficient solution with constant space complexity,
    # which involves using two pointers to traverse the linked list.

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        stack_length = 0
        current = head
        while current:
            stack.append(current)
            stack_length += 1
            current = current.next

        middle_node = head
        for i in range(stack_length // 2):
            middle_node = stack.pop()
        if stack_length % 2 == 1:
            middle_node = stack.pop()

        return middle_node


# Test cases
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    return values


solution = Solution()

# Test Case 1: Input: 1 -> 2 -> 3 -> 4 -> 5, Output: 3 -> 4 -> 5
head1 = create_linked_list([1, 2, 3, 4, 5])
middle1 = solution.middleNode(head1)
print(print_linked_list(middle1))

# Test Case 2: Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6, Output: 4 -> 5 -> 6
head2 = create_linked_list([1, 2, 3, 4, 5, 6])
middle2 = solution.middleNode(head2)
print(print_linked_list(middle2))
