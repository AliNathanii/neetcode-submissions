class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """We need to eliminate the duplicates in this example"""
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):  # cur is the current combination we have, pos is the current index we are at in nums list and target is the number we wanna add up to
            if target == 0:
                res.append(cur.copy())  # if the base case has been met append cur combination's copy to res!
                return
            elif target < 0:  # another base case
                return

            prev = -1  # initializing prev here
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:  # skip duplicates
                    continue
                cur.append(candidates[i])  # append each item in candidates to our cur combination
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()  # remove current candidate and call backtrack again

                prev = candidates[i]

        backtrack([], 0, target)
        return res

"""
It first sorts the candidates list to handle duplicates more easily. Then, it defines a helper function called backtrack that takes the current combination cur, the current position pos, and the remaining target target as its parameters.
The algorithm uses a recursive approach within this helper function. If the remaining target is zero, it means the current combination sums up to the target, and the combination is added to the result list.
If the target is less than zero, it returns to avoid unnecessary calculations. The function iterates through the candidates starting from the current position, skipping any duplicates by comparing the current candidate with the previous one.
For each candidate, it adds the candidate to the current combination, recursively calls the helper function with the updated combination, position, and reduced target, and then removes the candidate from the current combination (backtracking).
This process continues until all unique combinations are found. Finally, the algorithm returns the result list containing all valid combinations.
"""