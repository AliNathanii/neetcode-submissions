class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):  # gives us the position we wanna start at. Iterating in reverse until we get to last item
            cost[i] = min(cost[i] + cost[i + 1], (cost[i] + cost[i + 2]))  # first arg is the single jump, second arg is the double jump
        
        return min(cost[0], cost[1])  # this will work because we are guaranteed that the cost will have at least 2 elements

"""
It appends a 0 to represent the top of the staircase and iterates through the list in reverse, 
updating each step's cost to the minimum of taking one or two steps forward.
Finally, it returns the minimum cost of starting from either of the first two steps.
"""
# TC - O(n)
# SC - O(1)