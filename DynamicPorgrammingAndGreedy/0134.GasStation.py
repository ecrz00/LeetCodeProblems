'''
Approach:
Instead of evaluating each point as a start (which will require two nested loops) a greedy algorithm allows to solve it in a sigle pass. The solution has two key mathematical reasoning:
- If the total gas is less than the total cost, it's impossible to complete the circuit, regardless of where we start. 
- If we start at station A and run out of gas at station B, then none of the stations between A and B can be a starting point. Why? 'Cause if we arrived at any intermediate station with some gas (or even zero) and still couldn't get past B, it's impossible to reach B from any point after A .

Whenever the total gas grops below 0, we know that all previous stations are invalid starts. We then we reset the tank to 0 and set the next station as our new starting.

gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
diff = [-2, -2, -2, 3, 3]

- i=0: total = -2. < 0! idx = 1, total = 0
- i=1: total = -2. < 0! idx = 2, total = 0
- i=2: total = -2. < 0! idx = 3, total = 0
- i=3: total = 3.        idx = 3, total = 3
- i=4: total = 6.        idx = 3, total = 6

Final idx = 3.

Complexity:
- Time: O(n) -> One pass to sum, one pass to loop.
- Space: O(1) -> No extra space required.
'''
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    n = len(gas)
    if sum(gas)<sum(cost): return -1
    total = idx = 0
    for i in range(n):
        total+=gas[i]-cost[i]
        if total<0:
            total=0
            idx=i+1
    return idx