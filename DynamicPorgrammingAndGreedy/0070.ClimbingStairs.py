'''
Approach:
We will use Dynamic programminng, more specifically Tabulation. In this case, we have two base cases: 
- n = 1, we just have one possible way to climb a single step
- n = 2, we have two possible ways to climb  
If we continue computing the possible ways of reaching the top, we will find a sequence similar to the Fibonacci (1,2,3,5,...).
'''
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    prev = 1
    cur = 2
    for i in range(3,n+1):
        prev, cur = cur, prev+cur
    return cur