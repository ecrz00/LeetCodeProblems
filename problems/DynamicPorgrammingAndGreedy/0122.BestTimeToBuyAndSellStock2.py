'''
Approach: Greedy
The main idea is: If tomorrow's price is higher than today's, then buy today and sell tomorrow. If the price increases three days in a row, the sum of the daily differences is equal to buying at day 1 and selling at day 3.
The solution sums all the positive slopes (seeing in a graph, a positive slope means a profit), and doesn't sum the negatives.
prices = [1, 7, 2, 3, 6, 4]

- prices[1]=7, prices[0]=1. (7 > 1) -> profit += 6.  Current: 6
- prices[2]=2, prices[1]=7. (2 < 7) -> Skip.
- prices[3]=3, prices[2]=2. (3 > 2) -> profit += 1.  Current: 7
- prices[4]=6, prices[3]=3. (6 > 3) -> profit += 3.  Current: 10
- prices[5]=4, prices[4]=6. (4 < 6) -> Skip.

Final Profit: 10
        7
       / \       6
      /   \     / \    
     /     \   3   \ 
    /       \ /     \
   1         2       4
    (Gain:6) | (Gain:1+3) 
    
Complexity:
- Time: O(n) -> One single pass through the array.
- Space: O(1) -> No extra data structures used.
'''
def maxProfit(prices: list[int]) -> int:
    profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            profit+=prices[i]-prices[i-1]
    return profit