"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        def dfs(node):
            """
                0. if in nodeMap, return nodeMap[node]
                1. copy node, add to hashmap
                2. assign neighbors copy to new node
                3. return new node
            """
            if node in nodeMap:
                return nodeMap[node]
            newNode = Node(node.val)
            nodeMap[node] = newNode
            for neigh in node.neighbors:
                newNode.neighbors.append(dfs(neigh))
            return newNode
        return dfs(node) if node else None
                
        