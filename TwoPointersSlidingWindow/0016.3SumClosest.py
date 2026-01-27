'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
def threeSumClosest(nums: list[int], target: int) -> int: #T: O(n^2) S: O(1)
    nums.sort()
    current_min = -float('inf')
    n = len(nums)
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        low,high = i+1, n-1
        while low<high:
            possible_min = nums[i] + nums[low] + nums[high]
            if abs(possible_min - target) < abs(current_min - target):
                current_min = possible_min 
            if possible_min<target:
                low+=1
            elif possible_min>target:
                high-=1
            else:
                return possible_min
    return current_min