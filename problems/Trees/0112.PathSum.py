'''
Approach: 
We will perform a recursive DFS and at each level add or substract the value at the node. Since we are looking for leaf nodes, the sum needs to be propagated to the children until we hit a leaf.

For example, given a targetSum = 22

- Start at 5: summ=5. Not a leaf.
- Go Left to 4: summ=9. Not a leaf.
- Go Left to 11: summ=20. Not a leaf.
- Go Right to 2: summ=22. IS A LEAF. summ == targetSum? YES.
- Return True up the chain.

      5 (sum:5)
     / \
    4   8 (sum:13)
   /   / \
  11  13  4 (sum:17)
 /  \      \
7    2      1 (sum:18)
     ^ (sum: 5+4+11+2 = 22) -> FOUND!

Complexity:
- Time: O(n) -> In the worst case, we visit every node once.
- Space: O(h) -> Recursion stack depth equals the tree height.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    def hasSum(node, summ):
        if not node:
            return False
        summ += node.val
        if not node.left and not node.right: #when a leaf is found
            return summ == targetSum
        return hasSum(node.left, summ) or hasSum(node.right, summ)
    return hasSum(root,0)