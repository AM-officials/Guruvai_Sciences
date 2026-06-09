"""
Problem 1: LRU Cache Implementation

Logic and Approach:
To achieve strict O(1) time complexity for both get and put operations, this 
implementation utilizes a combination of a Hash Map and a Doubly Linked List.
We can also derive the solution in python using the collections.OrderedDict,
which would be more concise and efficient.

1. The Hash Map provides O(1) lookups, mapping keys to their exact node in memory.
2. The Doubly Linked List provides O(1) insertions and deletions. By maintaining 
   dummy 'left' (Least Recently Used) and 'right' (Most Recently Used) nodes, 
   we can instantly update an item's priority by snipping it out and moving it 
   to the MRU position without scanning the data structure.
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Dummy nodes to avoid out-of-bounds edge cases
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        """Inserts a node at the Most Recently Used (right) position."""
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        self.right.prev = prev.next = node

    def remove(self, node):
        """Removes a node from the linked list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Mark as recently used by moving it to the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Discard the Least Recently Used item from the left
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]