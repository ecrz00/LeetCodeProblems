'''
Approach: 
A valid BST must satisfy that, per node, the left-subtree only have smaller values and the right-subtree only have greater values.

Visual Trace:
      5 (min:-inf, max:inf)
     / \
    3   7
   / \
  1   4

- Node(5). Valid? Yes (-inf < 5 < inf) Go left.
- Node(3) Valid? Yes (-inf < 3 < 5). Go left.
- Node(1) Valid? Yes (-inf < 1 < 3). Left and right is None, return and go right.
- Node(4) Valid? Yes (3 < 4 < 5). Left and right is None, return and go right.
- Node(7) Valid? Yes (5 < 7 < inf). Left and right is None, the tree has been visited

Complexity:
- Time: O(n) -> Traverse the full tree once.
- Space: O(n) -> Recursion stack depth in worst case.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isValidBST(root: TreeNode) -> bool:
    def validate(node, minn, maxx):
        if not node: 
            return True
        if node.val <= minn or node.val >= maxx: 
            return False
        return validate(node.left, minn, node.val) and validate(node.right, node.val, maxx)
    return validate(root, float('-inf'), float('inf'))