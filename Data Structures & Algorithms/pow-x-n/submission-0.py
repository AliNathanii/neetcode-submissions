class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Given x, a float, raise to the power of n, which is given as an it"""

        ans = x **float(n)  # we cant use any built in libary function!

        return ans