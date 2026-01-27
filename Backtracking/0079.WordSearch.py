'''
Approach:
We will use backtracking (DFS). The algorithm explores all possible paths starting from each cell (i, j).

Visual Representation:
Board: [["A","B","C","E"],    Target Word: "ABCCED"
        ["S","F","C","S"],
        ["A","D","E","E"]]

Trace of the path:
1. Start at (0,0) 'A' -> Mark as '#'
2. Move Right to (0,1) 'B' -> Mark as '#'
3. Move Right to (0,2) 'C' -> Mark as '#'
4. Move Down to (1,2) 'C' -> Mark as '#'
5. Move Down to (2,2) 'E' -> Mark as '#'
6. Move Left to (2,1) 'D' -> Mark as '#' (FOUND!)

Visual Grid State during search:
   [ # ] — [ # ] — [ # ]   [ E ]
     |       |       |       |
   [ S ]   [ F ] — [ # ]   [ S ]
     |       |       |       |
   [ A ]   [ # ] — [ # ]   [ E ]
   
If the path fails, we "Unmark" (or perform a backtrack) by replacing '#' 
with the original character so other paths can use it.

Complexity:
- Time: O(N * 3^L) where N is number of cells and L is word length, and the 3 comes from 3 directions because we don't go back to the cell we just came from.
- Space: O(L) for the recursion stack depth.
'''
def exist(board: list[list[str]], word: str) -> bool:
    rows = len(board)
    columns = len(board[0])
    n=len(word)
    if rows==1 and columns==1:
        return board[0][0] == word
    def backtrack(pos: list[int], idx: int):
        i,j = pos 
        if idx == n:
            return True
        if board[i][j] != word[idx]: 
            return False
        char = board[i][j]
        board[i][j] = '#'
        for i_off, j_off in [(0,1),(1,0), (0,-1), (-1,0)]:
            row, col = i + i_off, j + j_off
            if 0 <= col < columns and 0<=row<rows:
                if backtrack((row,col),idx+1):
                    return True
        board[i][j] = char
        return False        

    for i in range(rows):
        for j in range(columns):
            if backtrack((i,j),0):
                return True
    return False