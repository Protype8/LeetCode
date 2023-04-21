class Page:
    def __init__(self,name="",prev=None,next=None):
        self.name = name
        self.prev = prev
        self.next = next
class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Page(homepage)
    def visit(self, url: str) -> None:
        self.current.next = Page(url,prev=self.current)
        self.current = self.current.next
    def back(self, steps: int) -> str:
        for i in range(0,steps):
            if(self.current.prev):
                self.current = self.current.prev
            else:
                break
        return self.current.name
    def forward(self, steps: int) -> str:
        for i in range(0,steps):
            if(self.current.next):
                self.current = self.current.next
            else:
                break
        return self.current.name


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
