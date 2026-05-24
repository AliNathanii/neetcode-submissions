class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        # union algorithm for find:
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]  # making parent of p, grandparent of p
                p = par[p]
            return p
        
        # union function implementation - have two functions and union them together
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:  # p1 will be parent of p2
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True  # if we were able to successfully union them together
        
        for n1, n2 in edges:
            if union(n1, n2) == False:
                return [n1, n2]
