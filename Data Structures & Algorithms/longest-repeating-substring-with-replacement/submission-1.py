class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Hashmap to count the occurence of each character.
        res = 0  # the longest substring found.

        l = 0  # lest pointer will be at the very beginning.
        # And our right pointer will go through the entire string:
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)  # for the character at position r we will increments its count by 1. If it doesnt exist in there yet we will have a defualt value of 0 be returned, that'll be incremented by 1.
            
            if (r - l + 1) - max(count.values()) > k:  # this condition checks if the current window size - count of the most frequent character exceeds k or not. Essentially verifies if more than k replacements would be required to make all characters in the current window the same.
                count[s[l]] -= 1  # if condition is True left pointer will be moved to right (next line) and in this line we Decrease the count of character at the left pointer before moving l. Why?  Because we need to maintain the Valid Window Size where no more than k replacements have to be made to make all characters in the window same. 
                l += 1
            
            res = max(res, r - l + 1)  # we wanna update our result to the max of its ever been. r- l + 1 is the size of the window.
        return res