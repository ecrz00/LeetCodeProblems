'''
Approach:
To avoid using extra space or another data structure, this solution performs three steps:
- Find the middle of the list: using a Floyd's Cycle-Finding algorithm with slow and fast pointers
- Reverse the second half: reverses the right half 'cauase the rearrangement requires the last element to become the second, the second-to-last to become the fourth, and so on.
- Merge both halves: Using the first half (from the start to middle) and the second half (the reversed right side) we merge them by alternating: one from the left, one from the right, and so on.

1 -> 2 -> 3 -> 4 -> 5
- Mid is 3:
    half1: 1->2->3 
    half2: 4->5
- Reverse half2: 5 -> 4
-Merge:
    1 -> 5 -> 2...
    1 -> 5 -> 2 -> 4 -> 3
    
Final: 1 -> 5 -> 2 -> 4 -> 3

Complexity:
- Time: O(n) -> Each step (find mid, reverse, merge) takes linear time.
- Space: O(1) -> Only pointers are manipulated.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reorderList(head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        half2 = slow.next
        prev = slow.next = None
        while half2:
            tmp = half2.next
            half2.next = prev
            prev = half2
            half2 = tmp
        half1, half2 = head, prev
        while half2:
            tmp1, tmp2 = half1.next, half2.next
            half1.next = half2
            half2.next = tmp1
            half1, half2 = tmp1, tmp2