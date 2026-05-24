class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        newset = set()

        #curr = head no need! Since this is an array and not a linked list with its head given.
        # in the next approach we use first pointer at 0 etc...
        for curr in nums:
            if curr in newset:
                return curr
            newset.add(curr)  # when adding to array we use arrayname.append(curr) but for adding to a set we use setname.add(curr)

"""
just like the previous question, it has SC O(N) which we could resolve using
two pointer approach of slow and fast pointers. The code itself however is simple to follow.
"""