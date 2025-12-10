'''
You are given an integer array nums.mA special triplet is defined as a triplet of indices (i, j, k) such that:
    0 <= i < j < k < n, where n = nums.length
    nums[i] == nums[j] * 2
    nums[k] == nums[j] * 2
Return the total number of special triplets in the array. Since the answer may be large, return it modulo 10^9 + 7.

    Enumample 1:
        Input: nums = [6,3,6]
        Output: 1
        Enumplanation: The only special triplet is (i, j, k) = (0, 1, 2), where:
            nums[0] = 6, nums[1] = 3, nums[2] = 6
            nums[0] = nums[1] * 2 = 3 * 2 = 6
            nums[2] = nums[1] * 2 = 3 * 2 = 6

    Enumample 2:
        Input: nums = [0,1,0,0]
        Output: 1
        Enumplanation: The only special triplet is (i, j, k) = (0, 2, 3), where:
            nums[0] = 0, nums[2] = 0, nums[3] = 0
            nums[0] = nums[2] * 2 = 0 * 2 = 0
            nums[3] = nums[2] * 2 = 0 * 2 = 0

    Enumample 3:
        Input: nums = [8,4,2,8,4]
        Output: 2
        Enumplanation: There are enumactly two special triplets:
            (i, j, k) = (0, 1, 3)
                nums[0] = 8, nums[1] = 4, nums[3] = 8
                nums[0] = nums[1] * 2 = 4 * 2 = 8
                nums[3] = nums[1] * 2 = 4 * 2 = 8
            (i, j, k) = (1, 2, 4)
                nums[1] = 4, nums[2] = 2, nums[4] = 4
                nums[1] = nums[2] * 2 = 2 * 2 = 4
                nums[4] = nums[2] * 2 = 2 * 2 = 4
'''
def specialTriplets(nums):
    freq_nxt = {}
    for num in nums:
        freq_nxt[num] = freq_nxt.get(num, 0) + 1
    freq_prev = {}
    counter = 0
    for num in nums:
        freq_nxt[num] -= 1
        if freq_nxt[num] == 0:
            del freq_nxt[num]
        target = 2 * num
        if target in freq_prev and target in freq_nxt:
            counter += freq_prev[target] * freq_nxt[target]
        freq_prev[num] = freq_prev.get(num, 0) + 1
    modd = 10**9+7
    return counter%modd


    

        
        

nums = [37,9,24,12,12,24,52,35]
a=specialTriplets(nums)
print(a)