class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count of what number occurs how many times:
        count = Counter(nums)
        
        # create a list of sublists where index of sublist will be count and inside the sublists will have numbers that occur sublist index times:
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)  # there we go

        # initialize res where we append n from freqs until len == k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:  # now traverse through each sublist
                res.append(n)
                if len(res) == k:
                    return res