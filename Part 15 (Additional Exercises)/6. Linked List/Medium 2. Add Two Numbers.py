from typing import Optional

# Date of Last Practice: Mar 4, 2024
#
# Time Complexity: O(N+M), where N is the number of nodes in the linked list 1,
#                  and M is the number of nodes in the linked list 2.
#
# Space Complexity: O(N+M+1), where N is the number of nodes in the linked list 1,
#                   and M is the number of nodes in the linked list 2.
#                   The "+1" accounts for an additional carry that
#                   might add an extra node to the result.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # This approach directly adds numbers from each node,
    # manages the carry as it traverses the lists,
    # and constructs the output list in a single pass,
    # making it both efficient and easier to understand.

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur_node = head = ListNode(None)

        carry = 0
        while True:
            l1_cur_val, l2_cur_val = 0, 0
            if l1:
                l1_cur_val = l1.val
                l1 = l1.next
            if l2:
                l2_cur_val = l2.val
                l2 = l2.next

            carry, out = divmod(l1_cur_val + l2_cur_val + carry, 10)
            cur_node.next = ListNode(out)
            cur_node = cur_node.next

            if l1 is None and l2 is None and carry == 0:
                break

        return head.next


class FirstSolution:
    # Same time and space complexity, but hard to understand.

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur_node = l1
        l1_reversed_val = 0
        l1_length = 0
        while cur_node:
            l1_reversed_val = l1_reversed_val * 10 + cur_node.val
            cur_node = cur_node.next
            l1_length += 1

        cur_node = l2
        l2_reversed_val = 0
        l2_length = 0
        while cur_node:
            l2_reversed_val = l2_reversed_val * 10 + cur_node.val
            cur_node = cur_node.next
            l2_length += 1

        l1_reversed_str = str(l1_reversed_val)[::-1]
        l1_val = int(l1_reversed_str) * (10 ** (l1_length - len(l1_reversed_str)))
        l2_reversed_str = str(l2_reversed_val)[::-1]
        l2_val = int(l2_reversed_str) * (10 ** (l2_length - len(l2_reversed_str)))
        sum = l1_val + l2_val

        sum_reversed_str = str(sum)[::-1]
        cur_node = head = ListNode(None)
        for char in sum_reversed_str:
            cur_node.next = ListNode(int(char))
            cur_node = cur_node.next

        return head.next


def list_to_linkedlist(elements):
    head = cur = ListNode(0)
    for el in elements:
        cur.next = ListNode(el)
        cur = cur.next
    return head.next


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Test case 1
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
assert linkedlist_to_list(result) == [7, 0, 8]

# Test case 2
l1 = list_to_linkedlist([0])
l2 = list_to_linkedlist([0])
result = Solution().addTwoNumbers(l1, l2)
assert linkedlist_to_list(result) == [0]

# Test case 3
l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linkedlist([9, 9, 9, 9])
result = Solution().addTwoNumbers(l1, l2)
assert linkedlist_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

print("All test cases passed!")
