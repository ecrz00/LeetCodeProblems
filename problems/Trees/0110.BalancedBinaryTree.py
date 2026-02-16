'''
Approach:
We will implement a Bottom-Up DFS to check balance and height simultaneously to achieve O(n) time complexity. First we will traverse the tree till reach its leafs, then we will return an list with a bool-value (representing if the left or right side is balanced) and the height (which is a 1 at any leaf). At the end, the function return only the bolean value.

Visual Trace (Balanced):
      1
     / \
    2   3
   /
  4
- Node 4: returns [True, 1]
- Node 2: left = [True, 1], right =[True, 0]. 
          abs(1-0) <= 1 is True. Returns [True, 2]
- Node 3: returns [True, 1]
- Node 1: l=[True, 2], r=[True, 1]. 
          abs(2-1) <= 1 is True. Returns [True, 3]

Visual Trace (Unbalanced):
      1
     / 
    2
   /
  3
- Node 3: [True, 1]
- Node 2: left =[True, 1], r=[True, 0]. Returns [True, 2]
- Node 1: l=[True, 2], r=[True, 0]. 
          abs(2-0) <= 1 is FALSE. Returns [False, 3]

Complexity:
- Time: O(n) -> We visit each node exactly once.
- Space: O(h) -> Height of the tree (recursion stack).
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isBalanced(root: TreeNode) -> bool:
    def dfs(node):
        if not node:
            return [True, 0]
        l,r = dfs(node.left), dfs(node.right)
        balanced = (l[0] and r[0] and abs(l[1]-r[1])<=1)
        return [balanced, max(r[1],l[1])+1]
    return dfs(root)[0]