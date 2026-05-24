class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Initialize result to 0
        for i in range(32):  # We are told that this will be a 32-bit number
            bit = (n >> i) & 1  # Extract the ith bit of n
            res += (bit << (31 - i))  # Shift the bit to its reversed position and add it to the result
        return res  # Return the reversed bit number


"""
This algorithm efficiently reverses the bits of a 32-bit integer by iterating over each bit, extracting it, shifting it to its new position in the reversed bit order, and accumulating the results. 
The use of bitwise operations ensures that the process is both fast and straightforward. 
The overall time complexity is O(1) because it always processes a fixed number of 32 bits. 
The space complexity is also O(1) as it uses a constant amount of extra space.

"""