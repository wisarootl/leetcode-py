from collections import OrderedDict

from leetcode_py.data_structures.doubly_list_node import DoublyListNode


class LRUCache:
    # Space: O(capacity)
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    # Time: O(1)
    # Space: O(1)
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move to end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    # Time: O(1)
    # Space: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add new
            if len(self.cache) >= self.capacity:
                # Remove LRU (first item)
                self.cache.popitem(last=False)

            self.cache[key] = value


class CacheNode(DoublyListNode[int]):
    def __init__(self, key: int = 0, val: int = 0) -> None:
        super().__init__(val)
        self.key = key


class LRUCacheWithDoublyList:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, CacheNode] = {}

        # Dummy head and tail nodes
        self.head = CacheNode()
        self.tail = CacheNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: CacheNode) -> None:
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: CacheNode) -> None:
        """Remove node from list"""
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def _move_to_head(self, node: CacheNode) -> None:
        """Move node to head (most recent)"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> CacheNode:
        """Remove last node before tail"""
        last_node = self.tail.prev
        assert isinstance(last_node, CacheNode), "Expected CacheNode"
        self._remove_node(last_node)
        return last_node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        # Move to head (most recent)
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            # Update existing
            node.val = value
            self._move_to_head(node)
        else:
            # Add new
            new_node = CacheNode(key, value)

            if len(self.cache) >= self.capacity:
                # Remove LRU
                tail = self._pop_tail()
                del self.cache[tail.key]

            self.cache[key] = new_node
            self._add_node(new_node)


# LRU CACHE IMPLEMENTATION STRATEGIES
#
# Strategy 1: OrderedDict (LRUCache)
# - Uses Python's built-in OrderedDict
# - move_to_end() for O(1) reordering
# - popitem(last=False) for O(1) LRU removal
# - Simple and clean implementation
#
# Strategy 2: HashMap + Doubly Linked List (LRUCacheWithDoublyList)
# - HashMap for O(1) key lookup
# - Doubly linked list for O(1) insertion/deletion
# - Manual node management with dummy head/tail
# - More complex but shows underlying data structure
#
# Both achieve O(1) time complexity for get() and put()
# Space complexity: O(capacity) for both approaches
