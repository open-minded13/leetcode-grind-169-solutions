# Date of Last Practice: Jan 9, 2024 -> Feb 22, 2024
#
# Time Complexity: O(1) because we use hash table and doubly linked list.
#
# Space Complexity: O(N), where N is the capacity of the LRU cache.


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.cache_size = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_front(self, node):
        if node.key in self.cache:
            node.prev.next = node.next
            node.next.prev = node.prev
        if node != self.head.next:
            node.next = self.head.next
            node.next.prev = node
            node.prev = self.head
            self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.move_to_front(node)
            self.cache[key] = node
            self.cache_size += 1
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)

        if self.cache_size > self.capacity:
            node_to_remove = self.tail.prev
            node_to_remove.prev.next = self.tail
            self.tail.prev = node_to_remove.prev
            del self.cache[node_to_remove.key]
            self.cache_size -= 1


class AnotherLRUCache:

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
