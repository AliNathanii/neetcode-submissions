class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])  # First get the dimensions of the board
        path = set()  # Can't revisit the same letter again. We use set() as it doesn't allow duplicates

        # Backtracking from here
        def dfs(r, c, i):
            """r, c is the position on the board and i will tell us the
            current character within our target word"""
            # Base cases: we found the word
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):  # All the invalid situations
                return False
            
            # At this point we have found the character we are looking for:
            path.add((r, c))  # With sets we use .add and not .append

            # Running dfs on all adjacent cells. Remember we only need to find our
            # target word once, if we do find it once, one of the 4 calls below will return True
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            path.remove((r, c))
            return res
        
        # Going through each position on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # If this ever returns True,
                    return True  # we immediately return True!
        return False  # If it doesn't, we return False here

"""
It first determines the dimensions of the board and initializes a set to track visited cells. 
The main logic is handled by a recursive depth-first search (DFS) function that explores all possible paths from each cell. 
The DFS function checks if the current cell is out of bounds, does not match the current character of the word, or has already been visited. 
If none of these conditions are met, it marks the cell as visited and recursively checks all four adjacent cells. 
If a valid path is found, it returns True; otherwise, it backtracks and continues the search. 
The algorithm iterates through each cell on the board, starting the DFS from each cell, and returns True if any DFS call finds the word. 
If no valid path is found after checking all cells, it returns False.


"""
