class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""  # this is the new string that we will add characters from given string

        for c in s:
            if c.isalnum():  # since we only want alpha numeric values in the string ie no spaces we first check for this. If yes then we add those values to our new string
                newStr += c.lower()  # we covert and add all characters to lower case as we are not case sensitive.
        if newStr == newStr[::-1]:  # if the new string is same as newstr reversed meaning it is a palindrome!
            return True
        else:
            return False
                