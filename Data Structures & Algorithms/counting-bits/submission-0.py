class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list of size n+1 with all elements set to 0
        # This list will store the number of 1-bits for each number from 0 to n
        dp = [0] * (n + 1)
        offset = 1  # This variable helps track the current power of 2

        # iterate over each number from 1 to n (including n!)
        for i in range(1, n + 1):
            # If i is a power of 2, update offset to be the current number i.
            # This is because the number of 1-bits resets at each power of 2.
            if offset * 2 == i:
                offset = i
            # The number of 1-bits in the current number i is equal to
            # 1 (for the bit added by offset) + the number of 1-bits in (i - offset).
            dp[i] = 1 + dp[i - offset]
        
        # Return the list dp which contains the number of 1-bits for each number from 0 to n
        return dp