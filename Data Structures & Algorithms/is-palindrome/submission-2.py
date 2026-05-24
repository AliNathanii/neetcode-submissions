class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s) - 1

        while l<r:
            while l<r and self.alphaNum(s[l]) == False:
                l += 1
            while r>l and self.alphaNum(s[r]) == False:
                r -= 1
                

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, char: str) -> bool:
        # Implement your logic here to determine if `char` is alphanumeric or a space
        # Example implementation:
        return char.isalnum()  # This checks if `char` is alphanumeric (letters or digits)