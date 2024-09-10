"""Learn to use linked list in Python by practicing with examples."""

import unittest
import io
from contextlib import redirect_stdout

# Date of Last Practice: July 1, 2023 -> Sep 5, 2023 -> Mar 20, 2024 -> Sep 10, 2024

# [Step-by-Step Tutorial]


class Node:
    """Node for a Linked List."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List Implementation."""

    def __init__(self):
        self.head = None

    # Add element to the Linked List
    def add(self, data):
        """Add a new node to the end of the linked list."""
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
        """Display the elements of the linked list."""
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    # Search for an Element in the Linked List
    def search(self, target):
        """Search for a target element in the linked list."""
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

    # Remove an Element from the Linked List
    # NOTE: The following method doesn't work because `current_node = current_node.next`
    #       only updates the local variable current_node and does not affect the actual
    #       linked list.
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
        """Remove the first occurrence of the target element from the linked list."""
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
        """Return the number of elements in the linked list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # Reverse a Linked List
    def reverse(self):
        """Reverse the linked list."""
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


# [Practice Makes You a Pro!] (class names and functions but not code)

# class Node:
#     """Node for a Linked List."""

#     # TODO: Define the __init__ method
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     """Linked List Implementation."""

#     # TODO: Define the __init__ method
#     def __init__(self):

#     # TODO: Define the add method
#     def add(self, data):

#     # TODO: Define the display method
#     def display(self):

#     # TODO: Define the search method

#     # TODO: Define the remove method
#     def remove(self, data):

#     # TODO: Define the length method
#     def length(self):

#     # TODO: Define the reverse method
#     def reverse(self):


# Test the Linked List Implementation
class TestLinkedList(unittest.TestCase):
    """Test cases for the LinkedList class."""

    def setUp(self):
        """Create a LinkedList object before each test."""
        self.linked_list = LinkedList()

    def test_add(self):
        """Test adding elements to the Linked List."""
        self.linked_list.add(10)
        self.linked_list.add(20)
        self.linked_list.add(30)

        self.assertEqual(self.linked_list.head.data, 10)
        self.assertEqual(self.linked_list.head.next.data, 20)
        self.assertEqual(self.linked_list.head.next.next.data, 30)

    def test_display(self):
        """Test displaying elements of the Linked List."""
        self.linked_list.add(10)
        self.linked_list.add(20)
        self.linked_list.add(30)

        # Capture printed output

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.linked_list.display()
        output = buffer.getvalue().strip().split("\n")

        self.assertEqual(output, ["10", "20", "30"])

    def test_search(self):
        """Test searching for elements in the Linked List."""
        self.linked_list.add(10)
        self.linked_list.add(20)
        self.linked_list.add(30)

        self.assertTrue(self.linked_list.search(20))
        self.assertFalse(self.linked_list.search(40))

    def test_remove(self):
        """Test removing elements from the Linked List."""
        self.linked_list.add(10)
        self.linked_list.add(20)
        self.linked_list.add(30)

        # Remove element in the middle
        self.linked_list.remove(20)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertEqual(self.linked_list.head.next.data, 30)

        # Remove head
        self.linked_list.remove(10)
        self.assertEqual(self.linked_list.head.data, 30)

        # Remove tail
        self.linked_list.remove(30)
        self.assertIsNone(self.linked_list.head)

    def test_length(self):
        """Test getting the length of the Linked List."""
        self.assertEqual(self.linked_list.length(), 0)
        self.linked_list.add(10)
        self.linked_list.add(20)
        self.assertEqual(self.linked_list.length(), 2)
        self.linked_list.add(30)
        self.assertEqual(self.linked_list.length(), 3)

    def test_reverse(self):
        """Test reversing the Linked List."""
        self.linked_list.add(10)
        self.linked_list.add(20)
        self.linked_list.add(30)

        self.linked_list.reverse()

        self.assertEqual(self.linked_list.head.data, 30)
        self.assertEqual(self.linked_list.head.next.data, 20)
        self.assertEqual(self.linked_list.head.next.next.data, 10)


# If running the test cases directly:
if __name__ == "__main__":
    unittest.main()
