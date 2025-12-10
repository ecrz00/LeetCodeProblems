'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
'''
def fourSum(self, nums: list[int], target: int) -> list[list[int]]: #T: O(n³) S: O(1)
    nums.sort()
    n=len(nums)
    res = []
    for i in range(n-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(n-2):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            lo, hi = j+1, n-1
            while lo<hi:
                summ = nums[i]+nums[j]+nums[lo]+nums[hi]
                if summ > target: hi-=1
                elif summ < target: lo+=1
                else:
                    res.append([nums[i],nums[j],nums[lo],nums[hi]])
                    lo,hi = lo+1, hi-1
                    while lo<hi and nums[lo] == nums[lo-1]: lo+=1
                    while lo<hi and nums[hi] == nums[hi+1]: hi-=1
    return res