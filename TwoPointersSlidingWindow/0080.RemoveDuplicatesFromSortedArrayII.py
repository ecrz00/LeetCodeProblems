'''
Approach: 
We will use a Two Pointers technique, maintaining a counter to ensure each unique number appears at most twice.

Visual Trace: nums = [1, 1, 1, 2, 2, 3]

Step-by-step:
1. i=1, nums[1]=1 (same as nums[0]): count=2. 
   count <= 2 is True -> nums[j=1] = nums[1], j becomes 2.
2. i=2, nums[2]=1 (same as nums[1]): count=3. 
   count <= 2 is False -> (Skip this 1, j stays at 2).
3. i=3, nums[3]=2 (different): count=1.
   count <= 2 is True -> nums[j=2] = nums[3], j becomes 3.
4. i=4, nums[4]=2 (same as nums[3]): count=2.
   count <= 2 is True -> nums[j=3] = nums[4], j becomes 4.
Final state of nums (first j elements): [1, 1, 2, 2, 3]. Return j = 5.

Complexity:
- Time: O(n) -> We visit each element exactly once.
- Space: O(1) -> Modification is done in-place.
'''
def removeDuplicates(nums: list[int]) -> int:
    n=len(nums)
    j=1
    count = 1
    for i in range(1,n):
        if nums[i]==nums[i-1]:
            count+=1
        else:
            count=1
        if count<=2:
            nums[j]=nums[i]
            j+=1
    return j