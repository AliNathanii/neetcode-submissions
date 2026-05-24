class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

"""
It first uses a dictionary (count) to tally the frequency of each number in the input list (nums). 
Then, it creates a list of lists (freq), where the index represents frequency, and the sublists contain the numbers that occur with that frequency. 
Iterating through freq in descending order, it appends the numbers to the result list (res) until it contains k elements.
This approach leverages a combination of counting and bucket sort techniques for efficient computation.
"""