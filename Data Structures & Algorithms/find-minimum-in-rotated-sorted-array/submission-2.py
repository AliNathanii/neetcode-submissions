class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initialize our result and the pointers.
        res = nums[0]  # could be any index from the array doesn't matter.
        l, r = 0, len(nums) - 1  # left pointer index being intialized to extreme left and r being initialized to exrtreme right.

        # now run the binary search while our pointers are in a valid order.
        while l <= r:
            if nums[l] < nums[r]:  # case 1: We got an already sorted array.
                res = min(res, nums[l])  # res will now hold minimum of itself and left most number.
                break
            
            # now if thats not the case thats when we will actually be doing binary search.
            m = (l + r) // 2  # calculating the mid pointer. Integer division.
            res = min(res, nums[m])  # res will now hold the minimum one of itself and the number at m index in nums array. This res is what will be returned after the while loop ie binary search has ended.

            # now we wanna know if we are gonna search to the right or the left.
            if nums[m] >= nums[l]:  # number at nums[m] is part of the left sorted portion!
                l = m + 1 # so we search in the right sorted portion by moving the left pointer to right of mid pointer by 1 unit.
            else:  # meaning we are in the right sorted portion, so we wanna look to the left portion now!
                r = m - 1  # right pointer is now mid - 1
        
        return res