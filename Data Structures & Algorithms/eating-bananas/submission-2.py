class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # l is the minimum speed aand r is the maximum speed that ie largest pile size. Speed cannot be 0 hence l is 1.
        res = r  # initializing the result with maximum possible speed. We are looking for the minimum one from pile that works, but we can initialize to max as we know that at least this will work.

        # performing the binary search
        while l <= r:
            k = (l + r) // 2  # k is the midpoint speed
            
            # Calculating the total hours required at speed k that we just calculated above.
            totalTime = 0  # initializing the total time.
            for p in piles:  # iterating over each pile.
                totalTime += math.ceil(float(p) / k)  # calculating the hours needed to eat the pile at speed k and then add it to totalTime. cein(arg1) converts arg1 to nearest whole number. Necessary as koko can only eat bananas inw whole numbers. Divides the number of bananas in the pile p by the eating speed k, giving the number of hours (which may be fractional) it takes to finish the pile.
            
            # now check if the total time is wihtin the allowed hours
            if totalTime <= h:
                res = k  # updating result with correct speed
                r = k - 1  # Try to find a smaller valid speed by adjusting the right boundary
            else:
                l = k + 1  # If k is too slow, adjust the left boundary to find a larger valid speed.
        
        return res  # at this point res contains the final ans/speed ie the minimum valid speed.