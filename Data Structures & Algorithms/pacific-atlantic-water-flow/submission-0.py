class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the grid
        ROWS, COLS = len(heights), len(heights[0])
        # Sets to keep track of cells that can reach the Pacific and Atlantic oceans
        pac, atl = set(), set()

        # Depth-first search (DFS) function
        def dfs(r, c, visit, prevHeight):
            # If the cell is out of bounds, already visited, or not reachable, return
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            # Mark the cell as visited
            visit.add((r, c))
            # Continue DFS in all four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Perform DFS from the Pacific ocean borders (top row and left column)
        for c in range(COLS):  # Loop over columns for the top row
            dfs(0, c, pac, heights[0][c])
        for r in range(ROWS):  # Loop over rows for the left column
            dfs(r, 0, pac, heights[r][0])

        # Perform DFS from the Atlantic ocean borders (bottom row and right column)
        for c in range(COLS):  # Loop over columns for the bottom row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):  # Loop over rows for the right column
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # List to store the coordinates of cells that can reach both oceans
        res = []
        # Check each cell to see if it can reach both the Pacific and Atlantic oceans
        for r in range(ROWS):  # Loop over all rows
            for c in range(COLS):  # Loop over all columns
                if (r, c) in pac and (r, c) in atl:  # If cell is in both sets, it can reach both oceans
                    res.append([r, c])
        
        # Return the result
        return res
