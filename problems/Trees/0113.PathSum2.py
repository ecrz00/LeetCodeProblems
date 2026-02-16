'''
Approach:
We will use DFS along with backtracking to store the solution path. The implementation uses two arrays: sol to compute partial solutions and res to store the final path.

When the function ends reaching in the node's childs we need to eliminate the node from the sol array before returning to the father. 

For example: targetSum = 22

      5 
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Path found: [5, 4, 11, 2] -> Sum = 22. Save copy!
Path found: [5, 8, 4, 5]  -> Sum = 22. Save copy!

Backtracking in action:
1. At node 2: sol = [5, 4, 11, 2]. It's a leaf, sum matches.
2. sol.pop() -> sol = [5, 4, 11]. Returning to node 11.
3. Node 11 finishes -> sol.pop() -> sol = [5, 4]. Returning to node 4.

Complexity:
- Time: O(n^2) -> In the worst case there could 
                 be O(n) paths, and copying each takes O(n).
- Space: O(h) -> where h is the height of the tree. For the recursion stack and the 'sol' list.
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def pathSum(root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        res = []
        def dfs(node, summ, sol):
            if not node:
                return
            sol.append(node.val)
            summ+=node.val
            if not node.left and not node.right and summ==targetSum:
                res.append(sol[:]) #store a copy, not just the reference
            dfs(node.left, summ, sol)
            dfs(node.right, summ, sol)
            sol.pop()
        dfs(root, 0, [])
        return res