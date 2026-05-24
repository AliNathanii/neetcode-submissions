class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q =  deque()  # initialize the queue -- which will only contain the rotten oranges
        time, fresh = 0, 0  # to keep a track of how much has passed and how many fresh oranges we have left

        ROWS, COLS = len(grid), len(grid[0])

        # iterate over the entire grid:
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:  # 1 represents fresh oranges, if thats whats in the cell increment the number of fresh!
                    fresh += 1
                if grid[r][c] == 2:  # if that cell says 2 meaning its a rotting orange so we append it to our queue on which we will run bfs
                    q.append([r, c])  # by appending we mean we will append coordinates [r, c]
        
        # we have successfully iterated through our grid
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # used for movement 
        while q and fresh > 0:  # loop will end if our queue gets empty or fresh oranges become 0 we stop!
            for i in range(len(q)):
                r, c = q.popleft()
                # now after having the coordinates of rotten orange popped, go through its neighboring cells in the grid:
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # if in bounds and fresh orange:
                    if (row < 0 or row == len(grid) or
                    col < 0 or col == len(grid[0]) or
                    grid[row][col] != 1):
                        continue  # continue to next iteration of the loop
                    grid[row][col] = 2  # make the current orange into a rotten orange!
                    q.append([row, col])  # and add that position into our queue
                    fresh -= 1  # decrement the number of fresh oranges
            time += 1  # since all that happened in a single iteration of time, at this point we will increment the time
        
        return time if fresh == 0 else -1
        # return time fresh == 0 otherwise -1 meaning we still have some oranges left that we just cant make rotten