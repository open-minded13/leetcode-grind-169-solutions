# Date of Last Practice: Jan 9, 2024
#
# Time Complexity: O(1), where N is the length of the string s.
#                  - get Operation (O(1)): Checking if a key exists in the nodes dictionary
#                    and accessing its corresponding node is an O(1) operation.
#                  - put Operation (O(1)): Checking if a key exists in the nodes dictionary is O(1).
#                    Adding a new node and adjusting pointers to make it the new head is O(1).
#                    In the case of exceeding capacity, removing the tail node and
#                    updating pointers is O(1).
#                  - move_to_front Method (O(1)): Involves only a fixed number of pointer changes,
#                    irrespective of the size of the cache.
#
# Space Complexity: O(N), where N is the length of the string s.
#                   The space complexity is primarily due to the dp array,
#                   which has a size of O(n).
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
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.head = None
        self.tail = None
        self.nodes = {}

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.move_to_front(key)
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            new_node = Node(key, value)
            self.nodes[key] = new_node
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.current_size += 1
        else:
            self.nodes[key].val = value
            self.move_to_front(key)

        if self.current_size > self.capacity:
            # Evict the least recently used node
            evicted_key = self.tail.key
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.nodes.pop(evicted_key, None)
            self.current_size -= 1

    def move_to_front(self, key):
        current_node = self.nodes[key]
        if current_node == self.head:
            return
        if current_node == self.tail:
            self.tail = current_node.prev
        if current_node.prev:
            current_node.prev.next = current_node.next
        if current_node.next:
            current_node.next.prev = current_node.prev
        current_node.next = self.head
        current_node.prev = None
        self.head.prev = current_node
        self.head = current_node


# Test Cases
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # cache is {1=1}
lru_cache.put(2, 2)  # cache is {1=1, 2=2}
assert lru_cache.get(1) == 1  # returns 1
lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
assert lru_cache.get(2) == -1  # returns -1 (not found)
lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
assert lru_cache.get(1) == -1  # returns -1 (not found)
assert lru_cache.get(3) == 3  # returns 3
assert lru_cache.get(4) == 4  # returns 4

print("All test cases passed!")
