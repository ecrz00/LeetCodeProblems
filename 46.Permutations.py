'''
Approach: We are going to use backtrack to solve this problem. Since all the numbers in nums are unique, we can check if num is already 
in the array. 
'''
def permute(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res, sol = [], []
    def backtrack():
        if len(sol) == n:
            res.append(sol[:])
            return
        for num in nums:
            if num not in sol:
                sol.append(num)
                backtrack()
                sol.pop()
    backtrack()
    return res