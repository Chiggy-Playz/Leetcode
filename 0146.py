import functools

from common import DoubleListNode


def log_return(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print(f"Method {func.__name__} returned: {result}")
        return result

    return wrapper


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: dict[int, int] = {}
        self.nodes: dict[int, DoubleListNode] = {}
        self.head = None
        self.tail = None

    @log_return
    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
        else:
            return -1

        if node.next:
            if self.tail == node:
                self.tail = node.next
            node.next.prev = node.prev
        if node.prev:
            if self.head == node:
                self.head = node.prev
            node.prev.next = node.next
            node.prev = self.head
        
        node.next = None
        assert self.head
        self.head.next = node
        node.prev = self.head
        self.head = node

        return self.data.get(key, -1)

    @log_return
    def put(self, key: int, value: int) -> None:

        self.data[key] = value
        if key in self.nodes:
            node = self.nodes[key]
        else:
            node = DoubleListNode(key)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            if node.next:
                if self.tail == node:
                    self.tail = node.next
                node.next.prev = node.prev
            if node.prev:
                if self.head == node:
                    self.head = node.prev
                node.prev.next = node.next
                node.prev = self.head
            
            node.next = None
            self.head.next = node
            node.prev = self.head
            self.head = node

        self.nodes[key] = node

        if len(self.data) > self.capacity:
            assert self.tail
            del self.data[self.tail.val]
            del self.nodes[self.tail.val]
            self.tail = self.tail.next
            if self.tail:
                self.tail.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lru = LRUCache(3)
lru.put(1,1) # 1
lru.put(2,2) # 1 2 
lru.put(3,3) # 1 2 3
lru.put(4,4) # 2 3 4
lru.get(4)   # 2 3 4
lru.get(3)   # 2 4 3
lru.get(2)   # 4 3 2
lru.get(1)   # 4 3 2
lru.put(5,5) # 3 2 5
lru.get(1)   # 3 2 5
lru.get(2)   # 3 5 2
lru.get(3)   # 5 2 3
lru.get(4)   # 5 2 3
lru.get(5)   # 2 3 5

