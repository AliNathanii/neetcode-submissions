class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Given x, a float, raise to the power of n, which is given as an it
        -- cannot use any built in function so implement factorial yourself"""

        # first case: n = 0
        if n == 0:
            return 1  # anything raised to the power 0 is 1

        if n < 0:  # if n is negative
            x = 1 / x  # base becomes resiprocal of itself
            n = -n  # n now becomes positive. We multiplied it by -ve sign
        
        result = 1
        for i in range(n):
            result *= x  # keep multiplying x which is the base by itself n number of times!

        return result

        