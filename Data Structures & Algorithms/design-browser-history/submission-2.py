class Node:
    def __init__(self, val,prev = None,next = None):
        self.val = val
        self.prev = prev
        self.next = next
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        # since we know we are at the curr node, we want to point to the next page we visit which is going to the be the url
        # and since it is double linked list, our prev is going to point back to the curr node
        self.curr.next = Node(url,self.curr)
        self.curr = self.curr.next
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -=1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)