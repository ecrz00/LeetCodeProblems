'''
Approach:
Traverse the whole array once, while iterating through the prices we keep track of the minimum price encountered so far and the maximum profit possible.
For example: [7, 1, 5, 3, 6, 4], min_price = 7, max_profit = 0
- 1 < 7 ? Yes -> min_price = 1, max_profit = 0
- 5 < 1 ? No -> max_profit = 4
- 3 < 1 ? No -> max_profit = 4
- 6 < 1 ? No -> max_profit = 5
- 4 < 1 ? No -> max_profit = 5

return 5  

Complexity:
- Time: O(n) -> We loop through the array exactly once.
- Space: O(1) -> Only two variables are used regardless of input size.

'''
def maxProfit(prices: list[int]) -> int:
    max_profit, min_price = 0, prices[0]
    for i in range(1, len(prices)):
        if prices[i]<min_price: 
            min_price = prices[i]
            continue
        else:
            max_profit = max(max_profit, prices[i]-min_price)
    return max_profit