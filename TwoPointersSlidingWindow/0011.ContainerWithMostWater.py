'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example: 
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water the container can contain is 49.
''' 
def maxArea(height: list[int]) -> int:
    lo, hi = 0, len(height)
    maxx = 0
    while lo<hi:
        cur = (hi-lo)*min(height[hi],height[lo])
        maxx = max(maxx, cur)
        if height[hi] > height[lo]:
            lo+=1
        else:
            hi-=1
    return maxx