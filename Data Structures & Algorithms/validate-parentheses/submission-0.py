class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        our_map = {")" : "(", "]" : "[", "}" : "{"}  # we mapped closing brackets as keys and opening ones as their values.

        # now we check for the closing brackets in given string.
        # when running a for loop in on dictionary or hashmaps, we basically through through the keys of dictionary.
        for c in s:
            if c in our_map:  # if c ie the character from s we are at, is already in our_map, will be checked as Key and in our case all keys are closing brackets and starting from a closing bracket does not make sense...
                if stack and stack[-1] == our_map[c]:  # does not make sense if key is already in our_map, and if stack is True ie not empty and stack[-1] == our_map[c] means value at the top of our stack is matching opening perenthesis.
                    stack.pop()  # if all above conditions are met meaning we found the matcing bracket so we can pop and continue going on.
                else:  # if the above conditions are not true ie if c is in our_map but either stack is empty or last added bracket in stack doesnt match the closing perenthesis we return False.
                    return False
            else:  # but if c is not in our_map ie we dont get a closing perenthesis and got an open perenthesis, we simply append it and it in our map.
                stack.append(c)  # we can add as many as we want.
        # once we have gone through all the characters, we can only return True if the stack is NOT EMPTY otherwise return False.
        return True if not stack else False
        