'''
Approach:
To keep track of the original and copy nodes this solution uses a dictionary to store their memory addresses. The linked list is traversed twice: once to build the dictionary and another to link nodes between them.

Complexity:
- Time: O(n) -> Two linear passes through the list.
- Space: O(n) -> To store the dictionary with 'n' nodes.
'''
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    if not head: return None
    dicti = {}
    cur = head
    while cur: #to build the dictionary
        new_node = Node(x=cur.val)
        dicti[cur] = new_node
        cur = cur.next 
    cur = head
    while cur: #to link nodes
        new_node = dicti[cur]
        new_node.next = dict[cur.next] if cur.next else None
        new_node.random = dicti[cur.random] if cur.random else None
        cur = cur.next
    return dicti[head]