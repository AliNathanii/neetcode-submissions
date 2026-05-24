class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        our_set = set()

        for r in range(len(s)):
            while s[r] in our_set:
                our_set.remove(s[l])
                l += 1
            our_set.add(s[r])
            res = max(res, r - l + 1)
        return res