'''
Approach:
To avoid extra time removing comas, full stops or white spaces, we will use a two pointers approach placing one at each end and moving them towards the center skipping non-alphanumeric characters.
Visual Trace: s = "A man, a plan, a canal: Panama"

- lo: "A", hi: "a" -> Match! (after .lower())
- lo: " ", hi: "m" -> lo is not alnum, lo+=1
- lo: "m", hi: "m" -> Match!
- ... skips "," and " " ...
- lo and hi meet in the middle.

Complexity:
- Time: O(n) -> Each character is visited at most once.
- Space: O(1) -> No extra strings or copies are created.
'''
def isPalindrome(s: str) -> bool:
    lo, hi = 0, len(s)-1
    while lo<hi:
        if not s[lo].isalnum():
            lo+=1
            continue
        elif not s[hi].isalnum():
            hi-=1
            continue
        if s[lo].lower()!=s[hi].lower():
            return False
        hi-=1
        lo+=1
    return True