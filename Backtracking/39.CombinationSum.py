'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Approach: Use recursive backtracking to build and store all the valid combinations that match the target
'''
def combinationSum(candidates: list[int], target: int) -> list[list[int]]: #T: O(n**t), S: O(n)
    res, sol = [], [] #sol is used to store each combination while building it, res is the list we will be returning
    def backtrack(idx, summ):
        if summ == target:
            res.append(sol[:]) #stores a copy
            return
        if summ>target or idx == len(candidates): 
            return 
        backtrack(idx+1, summ) #do not pick it
        sol.append(candidates[idx]) #pick it
        backtrack(idx, summ+candidates[idx]) 
        sol.pop() #reverse the decision
    backtrack(0,0)
    return res
        