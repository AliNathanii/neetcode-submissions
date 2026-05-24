class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array first
        # start with with a for loop and for that i, initiate two pointers and keep going...
        # use enumerate to keep track of index numbers

        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue  # move to next iteration if a is the same as prev number we were at
        
            l, r = i + 1, len(nums) - 1  # starting points of our points
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # found the right pair, now what? Return the numbers inside res list (we dont want the index numbers in this question)
                    res.append([n, nums[l], nums[r]])
                    l += 1  # move the pointer first and then we will add the case in case it is a duplicate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return res