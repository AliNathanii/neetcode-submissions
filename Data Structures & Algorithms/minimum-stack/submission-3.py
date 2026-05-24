class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp_stack = []
        mini = self.stack[-1]
        while len(self.stack):
            mini = min(mini, self.stack[-1])
            temp_stack.append(self.stack.pop())
        while len(temp_stack):
            self.stack.append(temp_stack.pop())
        return mini

        
