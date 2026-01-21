'''
Approach:
We will work with the matrix as a 1D sorted array, and use Binary Search to find the target value.
If we imagine the matrix unfolded into a single line, the total number of elements is rows * columns. Index 0 is matrix[0][0] and LastIndex is rows*columns - 1.
To convert a "virtual" mid-th position back to a (row, col) pair, we use:
- row: mid // columns (How many full rows fit into this index?)
- col: mid % columns (The remainder gives the position in the current row.)

Complexity:
- Time: O(log(m * n))
- Space: O(1)
'''
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows,columns = len(matrix), len(matrix[0])
    lo, hi = 0, rows*columns - 1
    while lo<=hi:
        mid = lo+(hi-lo)//2
        r,c = mid//columns, mid%columns
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            hi = mid-1
        else: lo=mid+1
    return False