class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.LRU = []

    def get(self, key: int) -> int:
        if key in self.data:
            self.LRU.remove(key)
            self.LRU.insert(0, key)
            return self.data[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            self.LRU.remove(key)
            self.LRU.insert(0, key)
        else:
            if len(self.data) >= self.capacity:
                lru_key = self.LRU.pop()
                del self.data[lru_key]
            self.LRU.insert(0, key)
            self.data[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)