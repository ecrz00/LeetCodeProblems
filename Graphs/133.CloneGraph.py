'''
Approach: 
Wi will perform a two-pass DFS with a hashmap:
- DFS helps us to copy nodes and then to connect them.
- The hashmap allows us to match an old node with the newer. With this strategy, we avoid infinite loops for visiting/creating a node we already have visited/created.

Complexity:
- Time: O(V + E) -> 'cause everything is visited twice
- Space: O(V) -> 'cause the dictionary store all the nodes and their copies
Where V is the number of nodes and E the number of edges.
'''
from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node: return None
    old2new = {}
    seen=set()

    def dfs(node):
        new_node = Node(node.val)
        old2new[node]=new_node
        for neighbor_node in node.neighbors:
            if neighbor_node not in seen:
                seen.add(neighbor_node)
                dfs(neighbor_node)
    
    dfs(node)
    for key in old2new:
        for neighbor in key.neighbors:
            old2new[key].neighbors.append(old2new[neighbor])
    return old2new[node]