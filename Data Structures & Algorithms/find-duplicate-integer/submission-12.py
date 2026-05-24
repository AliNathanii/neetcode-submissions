class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Brute force using a Hashmap now"""

        hashmap = {None: None}

        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1

        return -1