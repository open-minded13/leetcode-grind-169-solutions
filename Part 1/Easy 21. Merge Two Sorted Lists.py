# Date of Last Practice: Jun 19, 2023 -> Jan 25, 2024
#
# Time Complexity: O(N), where N is the total number of nodes in the linked list 1 and 2.
#                  This is because the solution iterates all the nodes in the linked list.
#
# Space Complexity: O(1). This is because it uses a constant amount of additional space.
#                   The method only utilizes a variable (current_result),
#                   regardless of the size of the input linked list.


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current_result = result_head = ListNode()
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current_result.next = list1
                current_result = current_result.next
                list1 = list1.next
            else:
                current_result.next = list2
                current_result = current_result.next
                list2 = list2.next
        if list1 != None:
            current_result.next = list1
        if list2 != None:
            current_result.next = list2
        return result_head.next


# Test Cases
# Test Case 1
# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4
# Merged List: 1 -> 1 -> 2 -> 3 -> 4 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

result = []
while merged_list != None:
    result.append(merged_list.val)
    merged_list = merged_list.next
print(result)  # Output: [1, 1, 2, 3, 4, 4]

# Test Case 2
# list1: 1 -> 2 -> 4
# list2: None
# Merged List: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = None

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

result = []
while merged_list != None:
    result.append(merged_list.val)
    merged_list = merged_list.next
print(result)  # Output: [1, 2, 4]

# Test Case 3
# list1: None
# list2: 1 -> 3 -> 4
# Merged List: 1 -> 3 -> 4
list1 = None

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

result = []
while merged_list != None:
    result.append(merged_list.val)
    merged_list = merged_list.next
print(result)  # Output: [1, 3, 4]

# Test Case 4
# list1: None
# list2: None
# Merged List: None
list1 = None
list2 = None

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

result = []
while merged_list != None:
    result.append(merged_list.val)
    merged_list = merged_list.next
print(result)  # Output: []
