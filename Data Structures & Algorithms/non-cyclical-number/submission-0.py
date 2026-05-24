class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)  # add the current number to our seen set
            summ = 0  # sum of squares initialized as 0
            for digit in cur:  # individual digit in the number n
                digit = int(digit)  # convert string to int
                summ += digit **2  # keep adding the sum of squares of digit
            if summ == 1:  # after the for loop, if sum == 1 return True
                return True
            cur = str(summ)  # Update the current number to the sum for the next iteration!
        


        # if the number is in seen meaing its an endless cycle therefore return False
        return False  