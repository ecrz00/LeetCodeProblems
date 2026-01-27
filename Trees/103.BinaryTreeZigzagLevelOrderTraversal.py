
'''
Approach: 
We will apply BFS to perform a level-order traversal using a queue, but we reverse the 'aux' list for every other level.

Visual Trace:
      1          <- Level 0: flip=1 (Normal)
     / \
    2   3        <- Level 1: flip=0 (Reverse)
   / \   \
  4   5   6      <- Level 2: flip=1 (Normal)

Execution:
Level 0: aux=[1]. flip=1 -> res=[[1]]. flip becomes 0.
Level 1: aux=[2, 3]. flip=0 -> res=[[1], [3, 2]]. flip becomes 1.
Level 2: aux=[4, 5, 6]. flip=1 -> res=[[1], [3, 2], [4, 5, 6]].

Order in Queue: Always left-to-right.
Order in Result: Alternates based on the 'flip' flag.

Complexity:
- Time: O(n) -> Each node is visited once.
- Space: O(n) -> To store the result and the queue.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    flip = 1 #1 for right to left, 0 for left to right
    if not root:
        return []
    q = deque()
    q.append(root)
    res=[]
    while q:
        aux = []
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            aux.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        if flip==0:
            res.append(aux[::-1])
        else:
            res.append(aux)
        flip^=1
    return res