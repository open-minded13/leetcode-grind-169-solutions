"""
A module that provides a solution to determine if a singly linked list
is a palindrome.

The module defines a ListNode class to represent each node in the singly linked 
list and a Solution class containing the method isPalindrome to check for 
palindrome properties in a linked list.

Typical usage example:

1. Define the linked list using the ListNode class.
2. Use the isPalindrome method of the Solution class to determine if the linked
   list is a palindrome.
3. Test the implementation using predefined test cases.
"""

# Date of Last Practice: Aug 12, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#
# Space Complexity: O(1), since we are using only a constant amount of space.

from typing import Optional


class ListNode:
    """Class for creating singly linked list nodes."""

    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.

        Args:
            val (int): The value of the node.
            next (ListNode): The next node in the linked list.
        """
        self.val = val
        self.next = next


class Solution:
    """Solution class to check if a linked list is a palindrome."""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determine if a singly linked list is a palindrome.

        Args:
            head (ListNode): The head of the linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.
        """
        # Step 1 - Use two pointers to find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2 - Reverse the second half of the linked list
        past, current = None, slow
        while current:
            tmp = current.next
            current.next = past
            past = current
            current = tmp
        right_head = past

        # Step 3 - Compare the first and second halves of the list
        left, right = head, right_head
        while left and right:
            if left.val != right.val:
                return False  # Not a palindrome
            left = left.next
            right = right.next

        return True  # It's a palindrome


def test_is_palindrome():
    """Test cases for isPalindrome method."""
    # Test Case 1: [1,2,2,1] should return True
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert Solution().isPalindrome(head1) is True

    # Test Case 2: [1,2] should return False
    head2 = ListNode(1, ListNode(2))
    assert Solution().isPalindrome(head2) is False

    # Test Case 3: [1] should return True (single node)
    head3 = ListNode(1)
    assert Solution().isPalindrome(head3) is True

    # Test Case 4: [1,0,1] should return True
    head4 = ListNode(1, ListNode(0, ListNode(1)))
    assert Solution().isPalindrome(head4) is True

    print("All test cases passed!")


if __name__ == "__main__":
    test_is_palindrome()
