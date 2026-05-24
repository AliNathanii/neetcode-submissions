class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:  # checking our minstack is not empty and already contains some items.
            val = min(val, self.minStack[-1])  # now val is the minimum value of val (arg) and the last item pushed into the minStack.
            self.minStack.append(val)
        else:  # if the minStack is empty.
             val = min(val, val)
             self.minStack.append(val)  # since the minStack was empty we append val to it.

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:  # will always be called when stack is not empty so no edge cases here.
        return self.stack[-1]  

    def getMin(self) -> int:  # again, will always be called when stack is not empty so no edge cases here.
        return self.minStack[-1]  # this will return from top of minStack as we want the minimum value.
        
