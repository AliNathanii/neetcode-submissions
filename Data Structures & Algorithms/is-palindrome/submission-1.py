class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # -1 for r as index starts from 0 in programming remember.
        
        while l < r:
            while l < r and not self.alphaNum(s[l]):  # l < r to make sure l doesno cross r and for the next one to make sure r doesnt cross l.
                l += 1  # move l to right it is NOT alphanumeric
            while r > l and not self.alphaNum(s[r]):  # both of these wile loops make sure that c is alphanumeric before we even compare the c at our pointers.
                r -= 1  # move r to left it is NOT alphanumeric.

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
        



    def alphaNum(self, c):  #  if c's ascii character is between A-Z's or a-z's or 1-9's that means its a valid character and not a blank space. We are supposed to ignore the blank space above in our algorithm.
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )