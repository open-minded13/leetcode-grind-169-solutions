"""
Merges k sorted linked lists into a single sorted linked list.

This module provides a class and method to merge multiple sorted linked lists.
The solution uses a min-heap for efficiency and assumes that the input lists
are sorted.
"""

from typing import List, Optional
from heapq import heappush, heappop

# Date of Last Practice: Jan 21, 2024 -> Feb 29, 2024 -> Oct 23, 2024
#
# Time Complexity: O(N * log K), where N is the number of all nodes, and K is the number
#                  of linked lists. We insert (heappush) and extract (heappop) once for
#                  each node. For each heap operation, we took O(log K) to complete
#                  since the max size of the min_heap is K.
#
# Space Complexity: O(K), where K is the number of linked list.


class ListNode:
    """Represents a node in a singly-linked list."""

    def __init__(self, val=0, next=None):
        """
        Initializes a ListNode with a given value and next node.

        Args:
            val (int): The value of the node. Defaults to 0.
            next (Optional[ListNode]): The next node in the list.
        """
        self.val = val
        self.next = next


class Solution:
    """Merges k sorted linked lists into a single sorted linked list."""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into a single sorted linked list.

        Uses a min-heap to efficiently find the smallest current node among the
        provided linked lists and merges them in ascending order.

        Args:
            lists (List[Optional[ListNode]]): List of ListNode objects, where each
                                              ListNode represents the head of a sorted
                                              linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        heap = []

        # Step 1 - Initialize the heap with the head node of each non-empty list.
        for list_id, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, list_id, head))

        new_head = ListNode()
        cur_node = new_head

        # Step 2 - Extract the smallest node from the heap and add to the merged list.
        while heap:
            _, list_id, node = heappop(heap)

            # Step 3 - If the popped node has a next node, push it to the heap.
            if node.next:
                heappush(heap, (node.next.val, list_id, node.next))

            cur_node.next = node
            cur_node = cur_node.next

        # Step 4 - Return the head of the merged linked list.
        return new_head.next


def list_to_linkedlist(lst):
    """
    Converts a list of integers to a linked list.

    Args:
        lst (List[int]): A list of integers.

    Returns:
        Optional[ListNode]: The head of the linked list.
    """
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    """
    Converts a linked list to a list of integers.

    Args:
        node (Optional[ListNode]): The head of the linked list.

    Returns:
        List[int]: A list of integers representing the linked list values.
    """
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


def main():
    """
    Demonstrates the use of the Solution class for merging k sorted linked lists.
    """
    sol = Solution()

    # Test Case 1 - Merging three sorted linked lists.
    lists = [list_to_linkedlist(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert linkedlist_to_list(sol.mergeKLists(lists)) == expected

    # Test Case 2 - Merging an empty list.
    lists = []
    expected = []
    assert linkedlist_to_list(sol.mergeKLists(lists)) == expected

    # Test Case 3 - Merging a list containing an empty list.
    lists = [list_to_linkedlist(l) for l in [[]]]
    expected = []
    assert linkedlist_to_list(sol.mergeKLists(lists)) == expected

    print("All tests passed!")


if __name__ == "__main__":
    main()
