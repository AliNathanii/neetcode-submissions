class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Non recursive approach ie iterative approach"""

        # Base case: Start with a list containing an empty list
        perms = [[]]

        # now we compute the subproblem
        for n in nums:  # we now wanna add this n to all the existing permutations
            new_perms = []  # Create a new list to store the new permutations
            # Insert n into every single possible position in the permutation p
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()  # create a copy of the current permutation
                    p_copy.insert(i, n)  # insert n at position i in the copy
                    new_perms.append(p_copy)  # add the new permutation to new_perms
            # update perms to new permutations we just created
            perms = new_perms
        return perms  # and now return perms which is the list of all permutations