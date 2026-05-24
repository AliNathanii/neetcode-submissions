class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force

        n = len(temperatures)
        result = [0] * n  # result array as large as the input array temperatures

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:  # if we find a warmer temp:
                    result[i] = j - i  # we calculate the difference in days so j - i, and that value is stored in result array at index i
                    break
        return result