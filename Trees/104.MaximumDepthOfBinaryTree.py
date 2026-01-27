'''
Approach: 
We can solve this problem in two different ways:
1. Recursive DFS (Post-order traversal) We compute the height of the leaves first and propagate the result upwards.
        1
        / \
        2   3
            \
            4

    - maxDepth(4) = 1 + max(0, 0) = 1
    - maxDepth(3) = 1 + max(0, 1) = 2  (Height of 4 + node 3)
    - maxDepth(2) = 1 + max(0, 0) = 1
    - maxDepth(1) = 1 + max(1, 2) = 3  <-- Final Result

    Complexity:
    - Time: O(n) - Visits every node.
    - Space: O(h) - Stack space (height of the tree).
2. Iterative BFS using a queue to count how many levels we can fully traverse before the queue is empty.
        1      -> Level 1 (res = 1)
        / \
        2   3    -> Level 2 (res = 2)
            \
            4  -> Level 3 (res = 3)

    Complexity:
    - Time: O(n) - Each node is enqueued and dequeued once.
    - Space: O(w) - Maximum width of the tree (max nodes in the queue).
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepthDFS(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return 1 + max(self.maxDepthDFS(root.left), self.maxDepthDFS(root.right))
    def maxDepthIter(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        res=0
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res+=1
        return res
        