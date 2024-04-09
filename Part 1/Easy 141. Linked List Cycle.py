# Date of Last Practice: Jun 23, 2023 -> Jan 28, 2024
#
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#                  This is because the worst case of the Floyd's Cycle Finding Algorithm
#                  iterates all the nodes in the linked list.
#
# Space Complexity: O(1). This is because it uses a constant amount of additional space.
#                   The method only utilizes a few variables (fast, slow),
#                   regardless of the size of the input linked list.


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Optimized Solution: Floyd's Cycle Finding Algorithm uses two pointers, slow and fast.
#                     The slow pointer moves one step at a time,
#                     while the fast pointer moves two steps at a time.
#                     If there is a cycle in the linked list, the fast pointer will
#                     eventually meet or catch up with the slow pointer
#                     within a limited number of iterations.
#                     The worst case is it iterates through all the nodes in the linked list once.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None or head.next.next == None:
            return False
        slow, fast = head, head.next.next
        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True


# This solution is also O(N) in time complexity and O(1) in space complexity.
# However, the solution modifies the original linked list
# by changing the next pointer of each visited node to a special "loop" node.
# This modification may have unintended side effects if the linked list is used in other parts of the program.
# Additionally, if the linked list is very long, this modification can consume a significant amount of memory.
class Other_Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        is_loop_node = ListNode("YES")
        while current != None:
            if current.val == "YES":
                return True
            next_node = current.next
            current.next = is_loop_node
            current = next_node
        return False


# Test Cases
# Create a linked list with a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # creates a cycle

solution = Solution()
print(solution.hasCycle(node1))  # Output: True

# Create a linked list without a cycle
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
print(solution.hasCycle(node1))  # Output: False

# Create a linked list with a cycle of length 1
node1 = ListNode(1)
node1.next = node1  # creates a cycle

solution = Solution()
print(solution.hasCycle(node1))  # Output: True

# Create an empty linked list
solution = Solution()
print(solution.hasCycle(None))  # Output: False
