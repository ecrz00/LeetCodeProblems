'''
Approach:
We try every possible substring starting from 'idx'. If it's a palindrome, we move to the next part of the string.

s = "aab"
backtrack(0):
   - i=0: "a" is pal? Yes. part=["a"]. Call backtrack(1)
     - i=1: "a" is pal? Yes. part=["a", "a"]. Call backtrack(2)
       - i=2: "b" is pal? Yes. part=["a", "a", "b"]. idx>=n! 
         -> Add ["a", "a", "b"] to res.
     - i=1: "ab" is pal? No.
   - i=1: "aa" is pal? Yes. part=["aa"]. Call backtrack(2)
     - i=2: "b" is pal? Yes. part=["aa", "b"]. idx>=n! 
       -> Add ["aa", "b"] to res.
   - i=2: "aab" is pal? No.

Complexity:
- Time: O(n * 2^n) -> In the worst case (all chars same), there are 2^N 
                     possible partitions, and checking each is O(n).
- Space: O(n) -> To store the recursion stack and the current partition.

'''
def partition(s: str) -> list[list[str]]:
    n=len(s)
    res,part=[],[]
    def isPalindrome(s: str) -> bool:
        lo,hi = 0, len(s)-1
        while lo<hi:
            if s[lo]!=s[hi]:
                return False
            lo+=1
            hi-=1
        return True
    def backtrack(idx: int):
        if idx>=n:
            res.append(part[:])
            return
        for i in range(idx, n):
            if isPalindrome(s[idx:i+1]):
                part.append(s[idx:i+1])
                backtrack(i+1)
                part.pop()
    backtrack(0)
    return res