class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        newset = set()

        #curr = head

        for curr in nums:
            if curr in newset:
                return curr
            newset.add(curr)
        