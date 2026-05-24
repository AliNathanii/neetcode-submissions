class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case when the given grid is empty:
        if not grid:
            return 0
        
        # get the dimensions
        rows, cols = len(grid), len(grid[0])
        visited = set()  # to keep track of cells visited
        islands = 0  # initialize the number of islands

        # our bfs algorithm that we will use to iterate over adjacent cells of the cell with "1" that we will find:
        def bfs(r, c):
            # bfs is not a recursive algorithm, it is an iterative algo hence we use ds queue
            q = collections.deque()
            visited.add((r, c))  # make sure to add this cell to our visited set
            q.append((r, c))  # fill up the queue with initial cell

            while q:
                row, col = q.popleft()  # while q is not empty popleft from it
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # possible directions that we wanna check "1" at
                for dr, dc in directions:
                    # for these positions first check whether they are inbound or not, is land or not, already visited or not -- if conditions met then we must run bfs on this cell as well!
                    if ((row + dr) in range(rows) and
                        (col + dc) in range(cols) and 
                        grid[row + dr][col + dc] == "1" and
                        (row + dr, col + dc) not in visited):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))  # and also add it to visited so that we don't visit it twice

        # iterate/visit all the cells in the grid now
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]  == "1" and (r, c) not in visited:  # nothing if we visit a 0, but if we visit a 1 that we hadn't visited before then:
                    bfs(r, c)  # apply bfs at that cell r, c
                    islands += 1  # since "1" is an island, increment the island counter

        return islands