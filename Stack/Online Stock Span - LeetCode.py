class StockSpanner:

    def __init__(self):
        self.queue = []
    def next(self, price: int) -> int:
        a = 1 
        while self.queue and self.queue[-1][0] <= price:
            s = self.queue.pop()
            a += s[1]
        self.queue.append((price,a))
        return a
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
