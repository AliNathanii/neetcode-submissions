class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count of what number occurs how many times:
        count = defaultdict(int)  # count dict will contain number as key and its count as the respective data
        for n in nums:
            count[n] += 1 
        
        # create a list of sublists where index of sublist will be count and inside the sublists will have numbers that occur sublist index times:
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)  # there we go

        # initialize res where we append n from freqs until len == k
        res = []
        for i in range(len(freq) - 1, 0, -1):  # traverse through freq mega list but in reverse order
            for n in freq[i]:  # now traverse through each sublist (n is individual int at this point)
                res.append(n)
                if len(res) == k:  # solution is guaranteed so we can keep checking for length of res until its k
                    return res