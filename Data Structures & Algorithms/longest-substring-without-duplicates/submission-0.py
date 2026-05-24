class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # first thing we need to do is to make a set to make sure we have all characters in our window.
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:  # if the character on right s[r] is already in our set we will have to update our window. How?
                charSet.remove(s[l])  # we remove that item from our set when it was added by the left pointer.
                l += 1  # now we update our left pointer to point to index 1, 2,3...etc.
            charSet.add(s[r])  # add the right pointer item to our set. We have made sure that it doesnt already exist in our set, if it did it has now been removed.
            res = max(res, r - l + 1)  # r - l + 1 is the currnt window size. We want res to be the bigger window size of the two.

        return res
        