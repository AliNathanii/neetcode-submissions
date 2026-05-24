class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []  # this stack will hold our paranthesis.
        res = []  # this is the result list that will be returned eventually.

        def backtrack(openN, closedN):  # no need to pass n, stack and res as they are considered global since this is a nested function. openN and closedN are counts of open and closed perenthesis we have already stacked in our stack.
            if openN == closedN == n:  # base case if openn and closedn and n are all same.
                res.append("".join(stack))  # python syntax for join all items in stack, join them together, from an empty string and once they have all been joined together they will form a complete string. And once that is done, we append that finished string to our result list.
                return  # return nothing as we want this funtion to not move forward and just move on to outside of this function.

            if openN < n:  # if we wann append an open paranthesis this the condition we wanna check.
                stack.append("(")
                backtrack(openN + 1, closedN)  # This is why we use backtracking/recursive here since now we wanna check the above conditon to see if base case has been satisfied. We add 1 to openN as we just appended an open paranthesis!
                stack.pop()  # pop the stack as we dont want the stack to keep holding all that we append.
            
            if closedN < openN:  # now if we wanna add a closed paranthesis this is the condition we want to me make sure is being met.
                stack.append(")")
                backtrack(openN, closedN + 1)  # checking to see if now the base condition is being satisfied or not. closedN + 1 as thats what we are appending this time.
                stack.pop()  # cleanup again by popping the character we just added.

        backtrack(0,0)  # calling the function with 0,0 as those are our defualt original starting counts before we append any paranthesis.
        return res  # but first call the backtracking function. (see now you realize why this function is called "backtrack")
 
 



