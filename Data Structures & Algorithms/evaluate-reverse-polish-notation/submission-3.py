class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                divident = int(b / a)
                stack.append(divident)
            else:  # must be a number!
                stack.append(int(c))
        
        # return the last appended number as we append the answer as soon as we run into an opperand
        return stack[-1]