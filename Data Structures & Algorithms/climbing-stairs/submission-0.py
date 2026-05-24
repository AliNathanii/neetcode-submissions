class Solution:
    def climbStairs(self, n: int) -> int:
        """Bottom up DP approach - starting at the bottom and working up"""
        # one is the number of ways to climb to the current step
        one, two = 1, 1  # two corresponds to the number of ways to climb to the previous step

        for i in range(n-1):  # this loop simulates moving from the base of the stairs to the nth step
            temp = one
            one = one + two  # one will now be the sum of two previous values
            two = temp  # two will become the old value of one

        return one  # finally one (the sum of two previous values) will be the final answer

"""
TC - O(n) as the loop runs n - 1 times
SC - O(1) no additional memory needed except one, two and temp and those are fixed amount of spaces
"""