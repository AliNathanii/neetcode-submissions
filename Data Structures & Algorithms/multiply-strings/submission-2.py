class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge Case: If either number is "0", the result is "0"
        if "0" in [num1, num2]:
            return "0"

        # Allocate an array of zeros with length equal to the sum of lengths of num1 and num2
        res = [0] * (len(num1) + len(num2))
        
        # Reverse num1 and num2 to facilitate multiplication from the least significant digit
        num1, num2 = num1[::-1], num2[::-1]

        # Iterate through each digit of num1
        for i1 in range(len(num1)):
            # Iterate through each digit of num2
            for i2 in range(len(num2)):
                # Multiply the current digits of num1 and num2
                digit = int(num1[i1]) * int(num2[i2])

                # Add the product to the current position in the result array
                res[i1 + i2] += digit
                
                # Handle carry over: Add the carry to the next position in the result array
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                
                # Keep only the last digit at the current position
                res[i1 + i2] = res[i1 + i2] % 10

        # Reverse the result array to correct the order of digits
        res, beg = res[::-1], 0
        
        # Initialize beg to skip any leading zeros in the result
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # Convert the remaining digits to strings
        res = map(str, res[beg:])
        
        # Join the digits into a single string and return it
        return "".join(res)
