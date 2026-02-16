'''
Approach: 
We will use DFS to perform a recursive in-order traversal (Left, Root, Right.)
Considering the following tree
      1
     / \
    2   3
   / \
  4   5

1. Start at 1 -> Go Left to 2
2. At 2 -> Go Left to 4
3. At 4 -> Left is None, Append [4], Right is None. (Back to 2)
4. Back at 2 -> Append [4, 2], Go Right to 5
5. At 5 -> Left is None, Append [4, 2, 5], Right is None. (Back to 1)
6. Back at 1 -> Append [4, 2, 5, 1], Go Right to 3
7. At 3 -> Left is None, Append [4, 2, 5, 1, 3], Right is None.

Complexity:
- Time: O(n) 
- Space: O(n)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def inorderTraversal(root: TreeNode) -> list[int]:
    res=[]
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res