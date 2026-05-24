class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:  # base case if the node is empty ie tree is empty
            return True
    
        # if we do have some nodes, we will next create an adjacency list as a dictionary / hashmap
        adj = {i : [] for i in range(n)}  # i will be value of that node, paired with an empty list as its value in the hashmap
        for n1, n2, in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            # appending both as the graph is Undirected ie both ways!
        
        visit = set()
        def dfs(i, prev):  # i is the value of noded we are visiting and prev is the previous node we are coming from
            if i in visit:
                return False  # loop detected!
            
            visit.add(i)

            # now lets go through every single neighbor of i and it is adjacency list that will contain all the neighbors
            for j in adj[i]:
                if j == prev:
                    continue  # skip this iteration
                if dfs(j, i) == False:  # i is what we are coming from so we will give this as the previous value to our dfs
                    return False
            return True  # no loop detected

        
        return dfs(0, -1) and n == len(visit)  # -1 as prev as we know it will never exist in the graph