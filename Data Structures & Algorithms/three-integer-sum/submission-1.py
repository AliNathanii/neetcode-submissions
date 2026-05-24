class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # remmeber the result will be returned as a list of lists.
        nums.sort()  # sort the input array

        # Now we will consider each value of the array as the possible first value of result. And then inside this we will run a sorted two sum algorithm.
        for i, a in enumerate(nums):  # i will be index value and a will be the int at that index posittion.
            if i > 0 and a == nums[i-1]:  # BASICALLY THIS SKIPS THE DUPLICATE! --  i > 0 meaning this is not the first value in input array if a is equal to the previous value then we will continue to the next iteration of the loop. This is done to not reuse the same int from nums.

                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])  # so by this point we have the modfied sorted two sum as our threeSum algorithm. 
                    # Updating the pointers now. Above if and elif statements actually do it for us. We only need to do in Else case.
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:  # if nums of left is equal to nums of left - 1 meaning the two nums values on left are the same, we increment l by 1. No need to do anything with r.
                        l += 1
        return res