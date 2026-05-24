class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Solving using DFS this time"""

        # lets deal with edge case empty grid or the first row is empty
        if not grid or not grid[0]:
            return 0

        # initialize what we will be using
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])  # dimensions of the grid

        def dfs(r, c):
            # check the for the base cases where we will return nothing
            if (
                r not in range(rows)  # r out out bounds
                or c not in range(cols)  # c out of bounds
                or grid[r][c] == "0"  # has "0" instead of "1" as we are looking for "1"s
                or (r, c) in visit  # or we have already visited this cell, in any of these cases we dont run dfs or just return
            ):
                return

            # the else case, its "1" and in bounds:
            visit.add((r, c))  # add this cell in visited set as a tuple
            # Apply DFS in the four possible directions individually -- another way, simpler than for loop!
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up



        # traversing through the grid and looking for "1"s:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    # increase island count and call dfs on this cell
                    islands += 1  # in this question we are just counting groups of 1 together (adjacent of each other)
                    dfs(r, c)
        
        return islands