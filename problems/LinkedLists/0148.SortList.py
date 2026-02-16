'''
Approach:
This solution splits the problem into three phases:
- Find the middle: Using a Floyd's Cycle-Finding algorithm with slow and fast pointers.
- Recursion: Dividing the list repeatedly till only individual nodes remain.
- Merge: Comparing the head of each half to connect the smallest node to a new list. If there are remaining nodes, they are cimply attached at the end.

[4, 2, 1, 3]
- Split -> [4, 2] and [1, 3]
- Split -> [4], [2] and [1], [3]
- Merge -> [2, 4] and [1, 3]
- Merge -> [1, 2, 3, 4]

Complexity:
- Time: O(n log n) -> Standard for Merge Sort.
- Space: O(log n) -> Due to the recursion stack.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        left = head
        right = self.getMin(head)
        tmp = right.next
        right.next = None
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMin(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        head = ListNode()
        cur = head
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur=cur.next
        cur.next = left if left else right
        return head.next