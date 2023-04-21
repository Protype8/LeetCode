import collections

class MyStack:
    def __init__(self):
        self.queue = collections.deque()
    def push(self, x: int) -> None:
        self.queue.append(x)
    def pop(self) -> int:
        return self.queue.pop()
    def top(self) -> int:
        a = self.queue.pop()
        self.queue.append(a)
        return a
    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
