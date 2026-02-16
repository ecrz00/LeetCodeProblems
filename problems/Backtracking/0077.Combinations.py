'''Approach: 
We will use backtracking (Depth-First Search)
Generate all possible combinations of k numbers from 1 to n by exploring a decision tree and backtracking when a path is complete.

Visual Trace (n=4, k=2):
Level 0:                    [ ]
                 /              \       \       \
Level 1:        [1]            [2]     [3]     [4]
               /  |   \       /  \      |       (no more numbers left)
Level 2:   [1,2][1,3][1,4] [2,3][2,4] [3,4]  <-- Result (len == k)


Complexity:
- Time: O(k * C(n, k)) where C(n, k) is the binomial coefficient.
- Space: O(k) for the recursion stack and the current solution list.
'''
def combine(n: int, k: int) -> list[list[int]]:
    res, sol = [], []
    def backtrack(idx):
        if len(sol) == k:
            res.append(sol[:])
            return
        for i in range(idx,n+1):
            sol.append(i)
            backtrack(i+1)
            sol.pop()
    backtrack(1)
    return res