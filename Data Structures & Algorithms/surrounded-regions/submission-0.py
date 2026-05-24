class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Not returning anything, only modifying the board in-place"""

        # get the dimensions of the board:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):  # main thing for recursive is the base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return 
            
            board[r][c] = "T"  # "O" here changed to a "T"
            capture(r + 1, c)  # now we will apply this capture method on call adjacent blocks!
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)


        # Phase 1: (DFS will only be needed here) Capture the unsurrounded regions O -> T
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1])):  # second condition is if it is a border cell ie r is 0 or ROWS - 1
                    capture(r, c)  # if the above condition is met -- we capture that cell!


        # Phase 2: Capture the surrounded regions remaining Os -> X - no dfs fairly simple
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Phase 3: Uncapture unsurrounded regions from phase 1 ie T -> 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"