class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # initialize the empty hashmap
        freq = [[] for i in range(len(nums)+1)]  # create an empty list, of empty lists (number of lists is the len of nums). This will be the frequency of how many times a number was present in the list.
        # this freq array will be the same size as the given array. This array will basically be of lists. This is part of the Bucket Sort (with a little trick) algorithm that we are using here!

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # counting the frequency of each number in nums and then adding 1 to its count after the loop finishes. 0 in case that number is not found in the list.
            # "count for this particular n value increases by 1, if n doesnt already exist we will get a 0.

        # next, we are gonna go through each value that we counted!
        for n, c in count.items():  # iterating through the heap count (must mention .items since we have a pair n, c) 
            freq[c].append(n)  # appending n ie the number/index from nums into the list we made above. What list within that list? One with the currect c value of the loop!
            # in the frq array at index count we will append to freq this value n. Meaning this value n occurs exactly c number of times.
        
        res = []  # this will be our output. We want the top K elements from freq.
        for i in range(len(freq) - 1, 0, -1):  # starting from last index, going all the way to 0, and last -1 so loop knows we are moving in reverse. We iterate through in descending order as we want to start with the number that occurs most frequently.
            for n in freq[i]:  # we will go through every value at index i in freq
                res.append(n)  # if the sublist freq[i] is not empty, we will append it to our results array.
                if len(res) == k:
                    return res