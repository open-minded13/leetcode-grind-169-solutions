import heapq
from typing import Optional, List

# Date of Last Practice: Jan 21, 2024 -> Feb 29, 2024
#
# Time Complexity: O(N * log K), where N is the number of all nodes,
#                  and K is the number of linked lists.
#                  We insert (heappush) and extract (heappop) once for each node.
#                  For each heap operation, we took O(log K) to complete
#                  since the max size of the min_heap is K.
#
# Space Complexity: O(K), where K is the number of linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        min_heap = []

        # The purpose of the `index` is in case the same number as `list.val`
        # is already in the heap. Without the `index` variable,
        # the heappush function will compare the next item, which is `list`.
        # However, `list` is an object and is not comparable.
        index = 0
        for list in lists:
            if list:
                heapq.heappush(min_heap, (list.val, index, list))
                index += 1

        root = ListNode(None)
        current = root
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                index += 1
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        return root.next


# Test Cases
def list_to_linkedlist(lst):
    dummy = ListNode(None)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


sol = Solution()

# Test Case 1
lists = [list_to_linkedlist(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]
expected = [1, 1, 2, 3, 4, 4, 5, 6]
assert linkedlist_to_list(sol.mergeKLists(lists)) == expected

# Test Case 2
lists = []
expected = []
assert linkedlist_to_list(sol.mergeKLists(lists)) == expected

# Test Case 3
lists = [list_to_linkedlist(l) for l in [[]]]
expected = []
assert linkedlist_to_list(sol.mergeKLists(lists)) == expected

print("All tests passed!")
