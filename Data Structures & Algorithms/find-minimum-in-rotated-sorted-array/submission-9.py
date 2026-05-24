class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1
        res = nums[0]

        while l<=r:
            if nums[l] < nums[r]:  # base case already sorted array so we:
                res = min(res, nums[l])  # update res and just break out of the for loop
                break
                
            m = (l + r) // 2  # base case not met so we perform binary search now and calc the mid point
            res = min(res, nums[m])  # update res to the smaller one of the two values
            if nums[l] <= nums[m]:  # update the pointer given left side is sorted or not. We move pointer away from the sorted side
                l = m + 1
            else:
                r = m - 1
        
        return res