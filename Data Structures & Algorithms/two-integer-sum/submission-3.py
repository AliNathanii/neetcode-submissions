class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # key: value, value: index of key

        for i, n in enumerate(nums):
            diff = target - n  # target is the number we will look for in the hashmap.
            if diff in prevMap:
                return [prevMap[diff], i]  # we return [prevMap[diff] which is index position of diff and i which is index position where we are right now]
            prevMap[n] = i  # if we move to this part of the code, we edit the hashmap. For this value n the index is i. So key is n is paired up with i.

