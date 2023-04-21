class FreqStack:
    def __init__(self):
        self.d = {}
        self.a = {}
        self.current_max = 0
    def push(self, val: int) -> None:
        current_value = self.d.get(val,0)+1
        self.d[val] = current_value
        if(current_value > self.current_max):
            self.current_max = current_value
        if(current_value in self.a):
            self.a[current_value].append(val)
        else:
            self.a[current_value] = [val]
    def pop(self) -> int:
        while not self.a[self.current_max]:
            self.current_max-=1
        s = self.a[self.current_max].pop()
        self.d[s]-=1
        if(not self.a[self.current_max]):
            self.current_max -= 1
        return s
