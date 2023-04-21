import collections
class MinStack:
    def __init__(self):
        self.queue = []
        self.mins = [float(inf)]
    def push(self, x: int) -> None:
        if(x <= self.mins[-1]):
            self.mins.append(x)
        self.queue.append(x)
    def pop(self) -> int:
        if(self.queue[-1] == self.mins[-1]):
            self.mins.pop()
        return self.queue.pop()
    def top(self) -> int:
        return self.queue[-1]
    def empty(self) -> bool:
        return len(self.queue) == 0
    def getMin(self) -> int:
        return self.mins[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
