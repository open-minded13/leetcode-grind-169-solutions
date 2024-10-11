"""
Provides two solutions to the "Remove Nth Node From End of List" problem on LeetCode.

The first solution uses two pointers to remove the nth node from the end of a 
singly-linked list in one pass. The second solution is an alternative approach 
that also uses two pointers but handles edge cases differently.
"""

from typing import Optional

# Date of Last Practice: Aug 24, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#                  Both solutions traverse the list once.
#
# Space Complexity: O(1), as both solutions use constant extra space.


class ListNode:
    """Represents a node in a singly-linked list.

    Attributes:
        val (int): The value of the node.
        next (Optional[ListNode]): The next node in the list, or None.
    """

    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        """Initializes a ListNode instance.

        Args:
            val (int): The value of the node. Defaults to 0.
            next (Optional[ListNode]): The next node in the list. Defaults to None.
        """
        self.val = val
        self.next = next_node


class Solution:
    """Remove the nth node from the end of a singly-linked list."""

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Removes the nth node from the end of the linked list in one pass.

        Args:
            head (Optional[ListNode]): The head of the singly-linked list.
            n (int): The position from the end of the list of the node to remove.

        Returns:
            Optional[ListNode]: The head of the modified list.
        """
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # Step 1 - Move fast pointer n+1 steps ahead.
        for _ in range(n + 1):
            fast = fast.next

        # Step 2 - Move both pointers until fast reaches the end.
        while fast:
            slow = slow.next
            fast = fast.next

        # Step 3 - Remove the nth node from the end.
        slow.next = slow.next.next

        return dummy.next

    def another_method(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Removes the nth node from the end of the linked list in one pass.

        Args:
            head (Optional[ListNode]): The head of the singly-linked list.
            n (int): The position from the end of the list of the node to remove.

        Returns:
            Optional[ListNode]: The head of the modified list.
        """
        slow, fast = head, head

        # Step 1 - Advance the fast pointer by n nodes.
        while fast.next:
            if n > 0:
                fast = fast.next
                n -= 1
                continue
            slow = slow.next
            fast = fast.next

        # Step 2 - If slow and fast are the same, the list has only one node.
        if slow == fast:
            return None

        # Step 3 - If n is still greater than 0, it means we need to remove the
        #          first node.
        if n > 0:
            return slow.next

        # Step 4 - Skip the nth node from the end.
        slow.next = slow.next.next

        return head


def test_remove_nth_from_end():
    """Tests for the removeNthFromEnd function."""

    # Step 1 - Helper function to create linked lists from a list.
    def create_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Step 2 - Helper function to convert linked list back to a Python list.
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Step 3 - Test case 1: Normal case with multiple elements.
    head = create_linked_list([1, 2, 3, 4, 5])
    n = 2
    result = Solution().removeNthFromEnd(head, n)
    assert linked_list_to_list(result) == [1, 2, 3, 5]

    # Step 4 - Test case 2: Single element list.
    head = create_linked_list([1])
    n = 1
    result = Solution().removeNthFromEnd(head, n)
    assert not linked_list_to_list(result)

    # Step 5 - Test case 3: Two-element list, remove the last element.
    head = create_linked_list([1, 2])
    n = 1
    result = Solution().removeNthFromEnd(head, n)
    assert linked_list_to_list(result) == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test_remove_nth_from_end()
