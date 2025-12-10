'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR". Write the code that will take a string and make this conversion given a number of rows:

Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

Example 3:
    Input: s = "A", numRows = 1
    Output: "A"
'''
def convert(self, s: str, numRows: int) -> str:
    if numRows==1:
        return s
    dir, i = 1, 0
    matrix = [[] for _ in range(numRows)]
    for c in s:
        matrix[i].append(c)
        if i == 0:
            dir=1
        elif i == numRows-1:
            dir-1
        i+=dir
    r = "".join(c for sublist in matrix for c in sublist)
    return r
    
