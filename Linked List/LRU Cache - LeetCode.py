from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity
        self.count = 0
    def get(self, key: int) -> int:
        a = self.od.get(key,-1)
        if a != -1:
            del self.od[key] 
            self.od[key] = a
        return a
    def put(self, key: int, value: int) -> None:
        if(key in self.od):
            del self.od[key]
            self.od[key] = value
        else:
            if(self.count < self.capacity):
                self.count += 1
            else:
                lru = next(iter(self.od.keys()))
                del self.od[lru]
            self.od[key] = value
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
