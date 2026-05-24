class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """We will use dfs and backtracking (removing the last added item in our subset)
        and then call the dfs function again!"""

        res = []  # what will be returned
        subset = []  # will be appended to our res above

        def dfs(i):  # dfs / backtracking function will get the index number of our curr/staring item
            """Will be called recursively to build all the possible subsets"""
            # base case:
            if i >= len(nums):  # meaning all items inside nums have been processed!
                res.append(subset.copy())  # append the current subset's copy to res list
                return # return nothing just end the function here
            
            # Otherwise
            subset.append(nums[i])  # include nums[i] item in the subset and append the number at index i in nums
            dfs(i + 1)  # Recursively call dfs to explore subsets starting from i + 1

            subset.pop()  # Backtrack: Remove the last element from subset (undo the inclusion of nums[i])
            dfs(i + 1)  #  and then Recursively call dfs again to explore subsets without nums[i]

        dfs(0)  # initialize with the very first index
        return res
        