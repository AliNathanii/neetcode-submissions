class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # this part was good.
            return False
        else:
            countS, countT = {}, {}  # two empty hashmaps created.

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)  # countS will count the occurence of each character in string s, s[i] is the key of the hashmap. Everytime we see a character we wanna increment its count by 1. get is a python function that has 2nd parameter the default count of that character. This is done to avoid key not found error.
                countT[t[i]] = 1 + countT.get(t[i], 0)  # same but for now hashmap countT and string t.
                # hashmaps built at this point.

            for c in countS:
                if countS[c] != countT.get(c, 0):
                    return False
            
            return True  # if we donnt return False anywhere above that means two given strings actually are anagrams.