class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Brute force using a set()"""

        record = set()

        for num in nums:
            if num in record:
                return num
            record.add(num)
        return -1