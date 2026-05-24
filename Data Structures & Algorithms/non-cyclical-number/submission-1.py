class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        cur = str(n)  # to make the given number n iterable!

        while cur not in seen:
            seen.add(cur)
            summ = 0
            for digit in cur:
                num = int(digit)
                summ += num **2
            if summ == 1:
                return True
            cur = str(summ)
        
        return False