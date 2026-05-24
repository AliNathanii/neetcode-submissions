class Solution:
    def isValid(self, s: str) -> bool:
        ourmap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:  # for each item in given string
            if c in ourmap:  # check if it is already in ourmap as a key
                if stack and stack[-1] == ourmap[c]:  # if yes then see if stack is not empty and its last value is same as mapped on ourmap
                    stack.pop()  # pop that top value if yes
                else:
                    return False  # else it means that Invalid Perenthsis!
            else:  # if c was not in our map? Append to our stack!
                stack.append(c) 
        
        if not stack:  # by the end if stack is empty, return True for valid perenthesis
            return True
        else:  # if it still contains something meaning Invalid Perenthesis hence return False
            return False
            
