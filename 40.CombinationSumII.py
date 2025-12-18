'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination. Note: The solution set must not contain duplicate combinations.
Approach: Use recursive backtrack to build all the possible combinations that sum to target. Since we need to pick each candidate at most once and also just return unique
combinations, we need to move our index while the numbers are the same
'''
def combinationSum2(candidates: list[int], target: int) -> list[list[int]]: #T: O(n*2^n), S: O(n)
    res, sol = [], []
    n = len(candidates)
    candidates.sort() # sort to easy avoid repeating numbers, takes O(nlogn) to sort
    def backtrack(idx, summ):
        if summ == target:
            res.append(sol[:])
            return
        if summ > target or idx == n:
            return
        nxt = idx+1
        while nxt<n and candidates[nxt] == candidates[idx]: nxt+=1
        backtrack(nxt, summ)
        sol.append(candidates[idx])
        backtrack(idx+1, summ+candidates[idx])
        sol.pop()
    backtrack(0,0)
    return res