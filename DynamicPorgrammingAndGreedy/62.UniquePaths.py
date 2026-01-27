'''
Approach:
For any cell (r,c) the number of unique paths is given by:
Paths(r,c) = Paths(r-1,c) + Paths(r,c-1)
This solution uses Dynamic Programming with a space-optimized 1D array.
Each cell value is the sum of the cell above it and the cell to its left.

The grid below shows the number of unique paths to reach each intersection.

    1 —— 1 —— 1 —— 1 —— 1 —— 1 —— 1  (Row 0: Only 1 way to go right)
    |    |    |    |    |    |    |
    1 —— 2 —— 3 —— 4 —— 5 —— 6 —— 7  (Row 1: 2 = 1+1, 3 = 2+1, etc.)
    |    |    |    |    |    |    |
    1 —— 3 —— 6 —— 10 — 15 — 21 — 28
    |    |    |    |    |    |    |
    1 —— 4 —— 10 — 20 — 35 — 56 — 84
    |    |    |    |    |    |    |
    1 —— 5 —— 15 — 35 — 70 — 126— 210
    |    |    |    |    |    |    |
    1 —— 6 —— 21 — 56 — 126— 252— 462 (Final result at top[-1])

How it works in the code:
- 'top' array stores the values of the current row being calculated.
- 'left' variable carries the value from the previous column.
- 'top[c] = left + top[c]' updates the value using both directions.

Complexity:
- Time: O(m * n)
- Space: O(n)
'''
def uniquePaths(m: int, n: int) -> int:
    top = [1]*n
    for r in range(1,m):
        left = 1
        for c in range(1,n):
            summ = left + top[c]
            left = top[c] = summ
    return top[-1]