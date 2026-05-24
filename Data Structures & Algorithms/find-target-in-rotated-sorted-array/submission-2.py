class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """In this approach we use the Binary Seach algorithm to 
        get a more efficient answer. Time Complexity O(logn)"""

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:  # its possible that middle value is the target, in that case we return the index.
                return mid  # eventually if the answer is there, above conditio will be met and this is where we will return the answer. It will also end the while loop.
            
            # If we are in the left sorted portion, if the mid value is greater than or equal to the left value.
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:  # if target is greater than the number at mid or less than the number in extreme left, in both case we have to see the right sorted side! Hence we move l to right of mid by 1.
                    l = mid + 1  # searching the right portion.
                else:  # means target is less than the middle AND greater than the left ie nums[l].
                    r = mid - 1  # searching the left portion, by moving r to left by mid - 1.
            
            # we are in right sorted portion of the array.
            else:  
                if target < nums[mid] or target > nums[r]:  # if target is less than the middle or greater than the extreme right:
                    r = mid - 1  # we go left and search the left sorted array.
                else:  # target is greater than the middle value AND is less than the number on extreme right.
                    l = mid + 1  # as we only have to search the right portion of the array.
        
        return -1  # if we find our result, it will be returned from above! If we dont then the while loop ends and this is where we return -1.


