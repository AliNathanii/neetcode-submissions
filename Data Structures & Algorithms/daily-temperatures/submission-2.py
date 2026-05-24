class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()  # we wont use stackTemp, only stackInd will be used
                res[stackInd] = i - stackInd  # this gives us the number of days until warmer weather is seen
            stack.append([t, i])
        return res