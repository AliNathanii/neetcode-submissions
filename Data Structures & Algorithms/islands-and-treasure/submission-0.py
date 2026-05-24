class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        # This is the helper function we will later use:
        def addGrid(r, c):  # conditions are imp, at point do we ____
            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
            (r, c) in visit or grid[r][c] == -1):  # r/c == ROWS/COLS would give out of bounds, rooms[r][c] == -1 is the obstacle
                return  # invalid and we dont add it 
            visit.add((r, c))
            q.append([r, c])

        # Start coding from here:
        # start by getting the dimensions:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()  # so that we dont visit the same node again
        q = deque()  # bfs is implemented using a queue
    
        # this is how we traverse through each node in a matrix
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:  # if the room at this r and c is 0 ie a gate
                    # then this position/grid will be added to our queue
                    q.append([r, c])
                    visit.add((r, c))  # so that we dont visit the same grid again
        
        dist = 0
        while q:  # now we can initialize dist as 0 and start traversing through the queue
            for i in range(len(q)):
                r, c = q.popleft()  # gate is what is being popped
                grid[r][c] = dist  # and at first gate will the distance
                # now to our queue add all the grids that are 1 distance away
                addGrid(r + 1, c)
                addGrid(r - 1, c)
                addGrid(r, c + 1)
                addGrid(r, c - 1)
            
            dist += 1  # everytime full layer is completed be sure to add increment the distance by 1

