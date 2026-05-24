class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Using DFS to traverse through the tree and apply it on each node"""

        # Step 1: Build the adjacency list ie at the end of this step our graph will be built
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)  # undirected graph therefore we do this way ...
            adj[n2].append(n1)  # ... including both n1 and n2 as each others' prereq
        
        # Step 2: Make a set to keep track of the visited nodes
        visited = set()

        # Step 3: DFS through the graph to traverse the graph, DFS is applied by recursion
        def dfs(node):
            if node in visited:  # checking if the node is already visited or not, if yes then just return nothing
                return 
            visited.add(node)  # add it to visit set if not in there
            # Traverse through the neighbors of the current node as we wanna apply dfs on them as well!!
            for neighbor in adj[node]:  # neighbors will be in our hashmap (the adjacency list) and they will be there as the value of given node as key
                if neighbor not in visited:  # applying DFS on each node that isnt in visited, the DFS function takes care of applying DFS on its neighbors
                    dfs(neighbor)
        
        # Step 4: Count the connected components
        count = 0
        for i in range(n):  # this loop will iterate over each node of the graph
            if i not in visited:  # check if i has already been visited -- if a node has not been visited meaning its part of the new connected component!
                dfs(i)  # it is at this point when we move to a different branch of nodes that we were on previously! See we are checking if it is Not in visited
                count += 1  # increment count everytime we run into a node that is not in visited!
        
        return count
