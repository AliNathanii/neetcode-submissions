class Solution:
    def findMin(self, nums: List[int]) -> int:
        """This is the brute force O(n) approach"""
        # initialize minimum element as the first item in the list.
        min_element = nums[0]

        for num in nums[1:]:  # we start iterating over nums array from the second item in the list thats why nums[1:]
            # update min_element if a smaller element is found.
            if num < min_element:
                min_element = num
        return min_element  # after the for loop ends, min_element will contain the smallest element.
        