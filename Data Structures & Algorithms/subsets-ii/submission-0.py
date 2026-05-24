class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """In this one, we cannot have any duplicates and the order doesnt matter"""
        
        res= []  # this is what we are gonna add our subsets to.
        nums.sort()  # sort the input array

        def backtrack(i, subset):
            """# we will keep track of i which is index where we are at in index array,
            and subset is what the subset is looking like so far"""

            # single base case when we have reached the end of the input array:
            if i == len(nums):
                res.append(subset[::])  # meaning we can take this subset we have built and append it to our res. But we do this with its copy. (can do using .copy() as well)
                return
            
            # recursive case - All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)  # pass in the next index and the current subset
            subset.pop()  # this will pop the value that we just added.

            # recursive case - All subsets that DONT include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:  # first condition makes sure we dont go out of bounds, in that case loop terminates and we move to the next line of code calling backtrack
                i += 1  # keep moving i until we dont have duplicates
            backtrack(i + 1, subset)  # now call backtrack on the next index

        backtrack(0, [])  # call the backtrack function initialized with 0 index and empty list
        return res

