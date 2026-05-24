class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Initialize result to 0
        for i in range(32):  # We are told that this will be a 32-bit number
            bit = (n >> i) & 1  # Extract the ith bit of n
            res += (bit << (31 - i))  # Shift the bit to its reversed position and add it to the result
        return res  # Return the reversed bit number


"""
This algorithm efficiently reverses the bits of a 32-bit integer.
It initializes a result variable res to 0. Then, it iterates through each of the 32 bits of the input integer n. 
For each bit, it uses (n >> i) & 1 to extract the ith bit of n. This operation shifts n right by i positions and isolates the least significant bit.
The extracted bit is then shifted to its new position in the reversed bit order using (bit << (31 - i)) and added to res. 
This process is repeated for all 32 bits. The final value of res contains the bits of n in reverse order. 
The time complexity is O(1) because it processes a fixed number of 32 bits, and the space complexity is also O(1) as it uses a constant amount of extra space.
"""