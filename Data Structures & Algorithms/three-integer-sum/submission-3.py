class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i -1]:
                continue

            l , r = i + 1, len(nums) - 1

            
            while l < r:
                threeSum = n + nums[l] + nums[r]  # must be calculated again at each while loop pointer movement
                if threeSum > 0:  # too big we gotta make it smaller
                    r -= 1
                elif threeSum < 0:  # too small gotta make it bigger
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l -1]:  # check again for duplication
                        l += 1
        return res