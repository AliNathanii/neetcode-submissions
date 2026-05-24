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


"""
The algorithm begins by checking for the edge case where either input string represents the number "0", in which case it returns "0". It initializes a result array with zeros, having a length equal to the sum of the lengths of the two input strings. 
This array will hold the intermediate and final results of the multiplication. Both input strings are reversed to facilitate the multiplication process from the least significant digit to the most significant digit. 
Nested loops iterate through each digit of the two reversed strings, multiplying them and adding the product to the appropriate position in the result array. 
Carry-over from each multiplication is managed by adding it to the next position in the result array. After the nested loops complete, the result array is reversed to correct the order of digits. 
Leading zeros are skipped, and the remaining digits are converted to strings, joined into a single string, and returned as the final result. This approach ensures accurate and efficient multiplication of two large numbers represented as strings.
"""