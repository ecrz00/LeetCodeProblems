'''
Approach: 
We will use backtracking (Binary Decision Tree), in which we have 2 options:
1. Exclude the element from the current subset.
2. Include the element in the current subset.

Visual Trace: nums = [1, 2]

Decision Tree:
                [] (idx 0)
               /  \
      Exclude 1    Include 1
            /        \
          []          [1] (idx 1)
         /  \        /  \
     Excl-2 Incl-2 Excl-2 Incl-2
      /      \      /      \
    []      [2]   [1]     [1,2] (idx 2 - Base Case)

The leaf nodes represent all possible subsets (The Power Set).

Complexity:
- Time: O(2^n * n) -> There are 2^n subsets, and copying each takes O(n).
- Space: O(n) -> The depth of the recursion stack.
'''
def subsets(nums: list[int]) -> list[list[int]]:
    res, sol = [],[]
    n = len(nums)
    def backtrack(idx):
        if idx == n:
            res.append(sol[:])
            return
        backtrack(idx+1)
        sol.append(nums[idx])
        backtrack(idx+1)
        sol.pop()
    backtrack(0)
    return res