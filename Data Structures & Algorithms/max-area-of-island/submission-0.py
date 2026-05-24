class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Easy question if you have a good understanding of DFS"""
        """We just have to tailor our dfs to solve the main problem in this question"""

        # our dfs algorithm which will go through adjacent cells of the given cell:
        def dfs(r, c):
            # base cases first with all revcursive functions:
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 0 or (r, c) in visit):
                return 0  # didnt find an island so 0
            
            visit.add((r, c))  # if above bases are not met we can proceed and add (r, c) as tupple into our visited set
            return (1 + dfs(r +1, c) + dfs(r -1, c)+ dfs(r, c+1)+ dfs(r, c-1))

        # get dimensions
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area

"""
The DFS function is designed to explore all connected '1's (land) starting from a given cell (r, c). When the function is called, it first checks if the current cell is out of bounds, contains '0' (water), or has already been visited. 
If any of these conditions are true, the function returns 0, indicating that this cell does not contribute to the island's area. 
If the cell is valid (i.e., it's land and hasn't been visited), it is marked as visited, and the function proceeds to recursively call DFS on the four adjacent cells (right, left, down, up). Each DFS call returns the area of the connected land in that direction. 
The function returns 1 (for the current cell) plus the sum of the areas returned by the DFS calls on the adjacent cells, effectively calculating the total area of the island connected to the starting cell.
"""