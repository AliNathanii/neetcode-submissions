class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # we realize that we will use a stack to solve this problem.

        for c in tokens:
            if c == "+":
                stack.append(stack.pop()+ stack.pop())  # if we run into operator + simply pop the last two items and add them.

            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)  # important: order of operation is that the second token will be subtracted, divided etc.
            
            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))  # even though when appending a digit string down, we already converted them to int but we apply it here again so that / instead of doing deceimal division, rounds to answer down to 0 as requested in the question.

            else:
                stack.append(int(c))  # if c is not an operator, simply convert it to an int and append or push it into our stack.d

        return stack[-1]