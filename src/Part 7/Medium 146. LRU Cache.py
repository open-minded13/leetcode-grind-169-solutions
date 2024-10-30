"""
LRU Cache implementation using a doubly linked list and hash map.

This module provides an efficient implementation of an LRU (Least Recently Used)
cache, which uses O(1) time complexity for both `get` and `put` operations by
combining a doubly linked list and a hash map. The linked list maintains the
order of usage, and the hash map allows for O(1) access to any node by key.

Example usage:

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
"""

# Date of Last Practice: Jan 9, 2024 -> Feb 22, 2024 -> Oct 29, 2024
#
# Time Complexity: O(1), where N is the length of the string s.
#                  - get Operation (O(1)): Checking if a key exists in the nodes
#                    dictionary and accessing its corresponding node is O(1).
#                  - put Operation (O(1)): Checking if a key exists in the nodes
#                    dictionary is O(1). Adding a new node and adjusting pointers to
#                    make it the new head is O(1). In the case of exceeding capacity,
#                    removing the tail node and updating pointers is O(1).
#                  - move_to_front Method (O(1)): Involves only a fixed number of
#                    pointer changes, irrespective of the size of the cache.
#
# Space Complexity: O(N), where N is the capacity of the cache.
#                   - Linked List (O(N)): Each node in the linked list holds a key,
#                     value, and two pointers, which occupy O(N) space.
#                   - Hash Map (O(N)): The nodes dictionary stores key-node pairs,
#                     which occupy O(N) space.
#
# Garbage Collection: In Python, when an object's reference count drops to zero
#                     (meaning there are no references to it in the program),
#                     it becomes eligible for garbage collection.
#                     This means that the memory occupied by the object can be freed.
#
#                     self.tail = self.tail.prev
#                     self.tail.next = None
#
#                     [Node A]↔[Node B]    >>   [Node A]→None    [Node B]
#                       ↑        ↑                  ↑
#                      head     tail           head & tail


class Node:
    """Represents a node in the doubly linked list."""

    def __init__(self, key, val):
        """Initializes a new node with key-value pairs and no pointers."""
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """An LRU cache with O(1) access using a hash map and doubly linked list."""

    def __init__(self, capacity: int):
        """
        Initializes the LRUCache with a set capacity.

        Args:
            capacity (int): The maximum number of elements the cache can hold.
        """
        self.capacity = capacity
        self.head = None  # Most recently used node
        self.tail = None  # Least recently used node
        self.nodes = {}  # Hash map to store key-node pairs

    def get(self, key: int) -> int:
        """
        Returns the value of the key if present, moves it to front of cache.

        Args:
            key (int): The key to access in the cache.

        Returns:
            int: The value associated with the key, or -1 if not found.
        """
        if key in self.nodes:
            self.move_to_front(key)
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Updates the key with the new value or adds a new key-value pair.

        If the cache exceeds capacity, removes the least recently used item.

        Args:
            key (int): The key to add or update in the cache.
            value (int): The value associated with the key.
        """
        # Add new node if key not present
        if key not in self.nodes:
            new_node = Node(key, value)
            self.nodes[key] = new_node

            # Add node to the head (most recent)
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            # Update existing node and move it to the front
            node = self.nodes[key]
            node.val = value
            self.move_to_front(key)

        # Ensure cache does not exceed capacity
        if len(self.nodes) > self.capacity:
            key_to_remove = self.tail.key
            # Remove tail node from the linked list
            if self.tail == self.head:
                self.tail = self.head = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            # Remove the evicted node from the hash map
            self.nodes.pop(key_to_remove, None)

    def move_to_front(self, key: int):
        """
        Moves the specified node to the front of the cache.

        Args:
            key (int): The key of the node to move to the front.
        """
        # Return if node is already the head
        if self.nodes[key] == self.head:
            return

        node = self.nodes[key]

        # If node is the tail, update the tail pointer
        if node == self.tail:
            self.tail = node.prev

        # Detach node from its current position
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # Move node to the head (most recent position)
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node


def main():
    """Demonstrates usage and runs assertions to verify LRUCache behavior."""
    cache = LRUCache(2)

    # Initial puts and get operation checks
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # Accessing 1 should make it most recent

    # Check for eviction of least recent key
    cache.put(3, 3)
    assert cache.get(2) == -1  # 2 was least recent and should be evicted

    # Add new item and check for the next eviction
    cache.put(4, 4)
    assert cache.get(1) == -1  # 1 was least recent and should be evicted
    assert cache.get(3) == 3  # 3 should still be present
    assert cache.get(4) == 4  # 4 should be the most recent and present

    print("All test cases passed!")


if __name__ == "__main__":
    main()
