class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)  # count array will be key, and its value will be string s

        for s in strs:
            count = [0] * 26  # this is done for each string inside the list -- count of letters
            for c in s:  # this is done to access each character inside that string
                count[ord(c) - ord("a")] += 1  # this count will be converted to tuple and then added as key in res dict
            key = tuple(count)
            res[key].append(s)  # the dict res, will have key as the key and s will be appended to that key's list data
        
        return res.values()  # by the end we just return the values of that dictionary and not the whole dictionary itself
            
"""
1. Go through each string s and initiate a count array [0] * 26
2. Go through each character c in that string s and increment its ascii value's count count[ord(c) - ord("a")] += 1
3. Once that increment is done, convert current count (inside the for loop) into a tuple called key
4. Append s to the key in the res defaultdict(list)
5. Return only the values of res dict
"""