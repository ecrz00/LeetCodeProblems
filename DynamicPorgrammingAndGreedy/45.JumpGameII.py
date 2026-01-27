'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
Approach:
    1. We can use backtrack to compute all the possible combinations of jumps to do. Also, store in a reference the minimum number of jumps. At the end we return that
    2. We can use a Greedy (Two Pointers/Range) algorithm. This implementation uses two "boundaries": 'far' tracks the farthest reachable point from the current range, and 
    'end' marks the limit of the current jump. When we reach 'end', we must jump again (which means increment the amount of jumps).
'''
def jump(nums: list[int]) -> int:
        smallest = 0
        n=len(nums)
        end, far = 0,0
        for i in range(n-1):
            far = max(far, i+nums[i])
            if i == end:
                smallest+=1
                end = far
        return smallest