class Solution:
    def hammingWeight(self, n: int) -> int:
        """Bit Manipulation again"""

        res = 0  # initialize the result variable
        while n:  # while n is True meaning not empty or while n > 0:
            res += n % 2  # n % 2 will either be 1 or 0. If 1 we wanna increment  res by 1
            n  = n >> 1  # bit shift to right by 1 and then make that the new n value
        return res