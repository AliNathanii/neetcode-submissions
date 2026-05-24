class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key for this one will be a pair of row/3 and c/3 ie (r/3, c/3)

        for r in range(9):  # iterating over rows with index r.
            for c in range(9):  # iterating over column now with index c.
                if board[r][c] == ".":
                    continue  # if the cell has . we will just ignore that and continue with that code.
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):  # here we are checking if the value is already in a column, row or one of the small enclosed squares.
                    return False
                
                cols[c].add(board[r][c])  # add the column value in board, if it was not found.
                rows[r].add(board[r][c])  # add the row value if not found.
                squares[(r//3, c//3)].add(board[r][c])  # add the value inside the enclosed square if not found.
        return True

"""remember that the given parameter list we know that first item is row and second is column thats why 
in the loop we can use board[r][c] to iterate through the board the way we are.
See how to add and look for a value in the hashmap.
In most of these questions, we start the empty hashset at top, look for the values we are 
looking for via a loop, and then if not found, add the value in the hashset and then the code continues!"""