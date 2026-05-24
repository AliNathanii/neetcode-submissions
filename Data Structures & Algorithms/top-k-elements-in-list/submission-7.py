class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        #count = defaultdict(int)
        #for n in nums:
        #    count[n] += 1

        freq = [[] for i in range(len(nums) + 1)]  # +1 because we wanna consider the situation where freq is 0
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0 , -1):  # traverse from end now ie right of mega freq list
            for j in freq[i]:  # access the sublist at i in mega list freq
                res.append(j)  # append that number to res 
                if len(res) == k:  # see if len of res is now k, return res if yes
                    return res  # return automatically breaks the iteration as well
