class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(t)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        
        for c in countT:
            if countS[c] != countT[c]:
                return False
        return True