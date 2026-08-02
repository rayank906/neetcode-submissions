"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        curr = head
        while curr:
            newNode = Node(curr.val)
            nodeMap[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            nodeMap[curr].next = nodeMap[curr.next] if curr.next else None
            nodeMap[curr].random = nodeMap[curr.random] if curr.random else None
            curr = curr.next
        
        return nodeMap[head] if head else None
        


"""
   1. first pass through linked list, make deep copy of nodes
   2. create a hashmap mapping original to deep copy
   3. second pass to connect the deep copies
        next pointers go to next node
        random pointers to random nodes
    4. hashmap used for O(1) access to deep copies of random nodes
    5. return val of nodeMap[head]
"""
        