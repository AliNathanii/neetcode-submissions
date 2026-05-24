class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:  # if we can add more open perenthesis based on openN value and n value, add em!
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()  # mandatory in backtracking to maintain state
            if closedN < openN:  # given openN's value, if we need to add closedN, add em!
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()  # mandatory in backtracking to maintain state

        backtrack(0,0)
        return res