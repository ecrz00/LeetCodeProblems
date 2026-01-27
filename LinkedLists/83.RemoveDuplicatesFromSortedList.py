'''
Since the linked list is sorted, all duplicate elements are adjacent.

Visual Trace: 1 -> 1 -> 2 -> 3 -> 3 -> None

- cur is at first '1' and cur.next is also '1', then cur.next = cur.next.next (skip the second 1)
    List: 1 -> 2 -> 3 -> 3 -> None

- cur is still at first '1' and cur.next is now '2', then cur = cur.next (move to node 2)


- cur is at '2' and cur.next is '3', then cur = cur.next (move to node 3)

- cur is at first '3' and cur.next is also '3', then cur.next = cur.next.next (skip the second 3)
        List: 1 -> 2 -> 3 -> None

Complexity:
- Time: O(n) -> We visit each node once.
- Space: O(1) -> We only use one pointer; modification is in-place.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head