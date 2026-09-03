class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self, value: int) -> None:
        # if self.stack:
            self.stack.append(value)
            if self.minStack:
                currentMin=min(value,self.minStack[-1])
            else:
                currentMin=value
            self.minStack.append(currentMin)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()