class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping the charCount of each string to the list of anagrams. Defualtdict(list) ie (list is the default value) for the edge case what if a count doesnot exist.

        for s in strs:  # going through each string in the strs
            count = [0] * 26  # initially we have 26 zeros since we havent iterated through the string yet so we have to initialize the count array and 26 simply becaause there are 26 letters in the alphabet (only considering lower case)

            for c in s:  # now we go through each character in the string we are in and change the count of the letters we find and map...
                count[ord(c) - ord("a")] += 1  # map a to index 0 and z to index 25 therefore we do this ascii conversion and subtraction. Increament by 1 as we are counting how many of each character do we have.

            res[tuple(count)].append(s)  # we wanna group together anagrams with this particular count (current iteration of the loop) and append them to the current count key. The list/array count was converted to key as python doesnot let you have a list or array as key.
        return res.values()

"""..."""