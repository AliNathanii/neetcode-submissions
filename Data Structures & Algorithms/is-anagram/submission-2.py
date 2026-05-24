class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1

        for c in countS:
            if countS[c] != countT[c]:
                return False
        
        return True