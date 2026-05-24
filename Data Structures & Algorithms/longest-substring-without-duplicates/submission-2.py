class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:  # -- bit if that item is in the set already
                charSet.remove(s[l])  # --- remove the item that l points at!
                l += 1  # --- and then move l by 1 unit to right
            charSet.add(s[r])  # we basically add all items in set --
            res = max(res, r - l + 1)
        return res