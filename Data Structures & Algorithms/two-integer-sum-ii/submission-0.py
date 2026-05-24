class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # setting our two pointers l starting from the left and r starting from right ie last item in the list.

        while l < r:  # technically no need for this while loop as we are guaranteed to find a solution as said in this question.
            curSum = numbers[l] + numbers[r]  # evaluate the current sum with the present placement of the pointers.

            if curSum > target:  # if surrent sum is larger than target meaning we gotta move right pointer to left (remember that the array is sorted!).
                r -= 1
            elif curSum < target:  # if smaller then move left pointer to right.
                l += 1
            else:  # in this case it means that they are equal! So just return the indices.
                return [l + 1, r + 1]  # + 1 because question says that we are working with - 1 indexes therefore just add 1 in your final answer.