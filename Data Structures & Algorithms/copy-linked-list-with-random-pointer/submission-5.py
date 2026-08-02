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
        nodeMap = { None: None}
        curr = head
        while curr: 
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = nodeMap[curr]
            copy.next = nodeMap[curr.next]
            copy.random = nodeMap[curr.random]
            curr = curr.next
        
        return nodeMap[head]
        


"""
   1. first pass through linked list, make deep copy of nodes
   2. create a hashmap mapping original to deep copy
   3. second pass to connect the deep copies
        next pointers go to next node
        random pointers to random nodes
    4. hashmap used for O(1) access to deep copies of random nodes
    5. return val of nodeMap[head]

    Edge case:
        null head: 
            make None:None mapping in hashmap
                solves case of null next and random ptrs too
"""
        