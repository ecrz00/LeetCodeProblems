'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition
Approach: The easiest way of solve this problem is using some sets to store and keep track of the number we've found. 
-First we are goind to validate the rows and then the columns 
-Finally, validate each box (3x3)
For this problem, all the sudokus are 9x9, so we can just simplify the time and space analysis to O(1). 
'''
def isValidSudoku(board: list[list[str]]) -> bool: #T: O(1), S: O(1)
    for i in range(9):#validate rows and columns
        rs=set() #stands for column set
        cs=set() #stands for row set
        for j in range(9):
            r_item = board[i][j]
            c_item = board[j][i]
            if r_item in rs:
                return False
            elif r_item != '.':
                set.add(r_item)
            if c_item in cs:
                return False
            elif c_item != '.':
                cs.add(c_item)
    boxes = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    for i,j in boxes:
        s = set()
        for row in range(i,i+3):
            for col in range(j,j+3):
                item = board[row][col]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
    return True

                