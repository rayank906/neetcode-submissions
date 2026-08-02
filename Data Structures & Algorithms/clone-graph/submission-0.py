"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
    
        oldtoNew = {}

        def dfs(node):
            newNode = Node(node.val)
            oldtoNew[node] = newNode
            for n in node.neighbors:
                if n in oldtoNew:
                    newNode.neighbors.append(oldtoNew[n])
                else:
                    newNode.neighbors.append(dfs(n))
            return newNode
        
        return dfs(node)

"""
    0. if not node, return None
    1. init hashmap
    2. make a copy of curr node and add to hashmap
    3. loop through is neighbours to make copies of them by recursively
    calling cloneGraph
    4. once we've finished recursing, we return back to the function
    and we can return the new node

    TimeC: O(n)
    SpaceC: O(n)
"""
        