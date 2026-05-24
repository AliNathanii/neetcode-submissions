class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""  # initializing our result string that we will be returning.
        for s in strs:
            res+= str(len(s)) + "#" + s  # this is how we are doing the encoding -- length of s as string + delimeter # + s itself. The we append it to our res string and return it.
        return res

    def decode(self, s: str) -> List[str]:  # here we decode the encoded res which is a single string and we have to return decoded list containing multiple string as items.
        res = []  # Initialize an empty list to store the decoded strings.
        i = 0  # Initialize a pointer i to keep track of the current position in the string s.

        while i < len(s):  # continue the loop as long as i is less than the length of s.
            j = i  # another pointer j at the current position of i.
            while s[j] != "#":  # finding the position of the delimiter.
                j += 1
            length = int(s[i:j])  # the substring s[i:j] ie substring s from index i to j is basically the word! And we find its length and convert it to int to get the length of the word.
            i = j + 1  # Move i to the start of the actual string, which is right after the delimiter.
            j = i + length  # Move j to the end of the current string using the length we just extracted.
            res.append(s[i:j])  # appending the substring s[i:j] to the result list!
            i = j  # Move i to the next position after the current string to continue decoding.
        
        return res  # res will contain all the decoded strings.

