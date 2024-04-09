# Date of Last Practice:
#   July 1, 2023 -> Sep 5, 2023 -> Mar 20, 2024


# Create a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add element to the Linked List
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # Traverse the Linked List
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    # Search for an Element in the Linked List
    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

    # Remove an Element from the Linked List
    # NOTE: The following method does not work because "current_node = current_node.next"
    #       only updates the local variable current_node and does not affect the actual linked list.
    #
    # def remove(self, target):
    #     if self.head == None:
    #         return
    #     current_node = self.head
    #     while current_node != None:
    #         if current_node.data == target:
    #             current_node = current_node.next
    #             return
    #         current_node = current_node.next
    def remove(self, target):
        if self.head is None:
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next

    # Get the length of the Linked List
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # Reverse a Linked List
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


# [Practice Makes You a Pro!]

# Create a Linked List

# Add element to the Linked List
# Traverse the Linked List
# Search for an Element in the Linked List
# Remove an Element from the Linked List
# Get the length of the Linked List
# Reverse a Linked List
