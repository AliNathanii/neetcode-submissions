class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Lets start by counting the frequencies of numbers in the list
        count = Counter(nums)
        # or:
        # count = {}
        # for num in nums:
        #     count[num] += 1

        # Make a list of lists:
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        # Traverse through the freq list IN REVERSE (ie starting from last and move left) and populate the result list that we will return 
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res