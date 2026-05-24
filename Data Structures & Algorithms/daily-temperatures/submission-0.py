class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # initiliazing this many zeros so that if no res found for some our res list already contains a 0 in their places.
        stack = []  # will hold Pair of values temp, index (not a dictionary tho just pairs like (,) or [,] but not dictionaries)

        for i, t in enumerate(temperatures):  # i is index value of the iteration we're at and t is the temperature value at thaty index.
            while stack and t > stack[-1][0]:  # while the stack is NOT empty ie contains something and t value we're at is greater than the t value [0] at the top of the stack [-1]:
                stackT, stackInd = stack.pop()  # stackT is now temp value from the pair popped, and stackInd is the index number of that value we just popped.
                res[stackInd] = i - stackInd  # subtracting the current number of index i and index popped from the stack stackInd and it will give us the number of days until warmer temp is observed.
            stack.append([t, i])  # while loop has ended so we just append temp and index pair into our stack. Meaning in its first iteration while loop will be skipped and then from second iteration of for loop while loop will possibly come into action.
        return res  # after the for loop ends res list will contain our values we want.