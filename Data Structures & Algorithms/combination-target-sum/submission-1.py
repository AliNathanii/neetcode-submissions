class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Combination (we are not doing permutation!) meaing backtracking"""
        # max height could be the target number
        
        res = []

        def dfs(i, cur, total):  # function will get starting pointer i, curr list (what values have we already added) and the total sum of those items in our cur list.
            # Base case 1:
            if total == target:
                res.append(cur.copy())  # if we do end up finding the target, copy curr list into our res list
                return  # make sure to return nothing after appending
            # Base case 2:
            if i >= len(nums) or total > target:  # if we have processed all the items in our list or total's value exceeds the target value
                return   # return nothing just end this function
            
            # Recursive Calls:
            cur.append(nums[i])  # add current candidate to our cur list
            dfs(i, cur, total + nums[i])
            cur.pop()  # now we will pop the last added item ie nums[i]
            dfs(i + 1, cur, total)  # i not included, i will now point at n + 1 thats why total remained just total, and process i + 1 now as we just popped i!

        dfs(0, [], 0)
        return res

"""If you notice, for backtracking we call the dfs function recursively, first after appending present i,
then we pop it and then again call the function recursively and update the parameters"""