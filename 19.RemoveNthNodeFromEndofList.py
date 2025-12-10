'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

       +---+    +---+    +---+    +---+    +---+
       | 1 | -> | 2 | -> | 3 | -> | 4 | -> | 5 |
       +---+    +---+    +---+    +---+    +---+
                          ^         |         ^
                          |         |         |
                          +---------+---------+
                                    |
                                    v
       +---+    +---+    +---+              +---+
       | 1 | -> | 2 | -> | 3 | ------------>| 5 |
       +---+    +---+    +---+              +---+
    
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head: ListNode, n: int) -> ListNode: #T: O(n) S: O(1)

    hd = ListNode(0, head)
    ahead, behind = hd
    for i in range(n+1):
        ahead = ahead.next
    while ahead:
        ahead = ahead.next
        behind = behind.next
    behind.next = behind.next.next
    return hd.next