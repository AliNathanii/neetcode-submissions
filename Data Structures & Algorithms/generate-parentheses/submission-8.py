class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
            if openN < n:  # first generate openN as we can as many as n
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()  # we always do this after calling backtracking, to preserve the state of the stack
            if closeN < openN:  # now generate closeN with respect to the openNs generated, to close all the open ones we generated!
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res