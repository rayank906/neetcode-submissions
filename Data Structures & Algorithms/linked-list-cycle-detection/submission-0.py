# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return False
        p1, p2 = head, head
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next.next
            if p1.val == -1:
                return False
            if p1 == p2:
                return True
        return False
        

"""
    1. make two pointers to the start
    2. p1 moves 1 at a time, p2 moves at twice the speed
    3. if p1 and p2 meet before p1 reaches nullptr, there exists a cycle
    4. elif p1 reaches -1, there is no cycle

    Edge cases:
        if single node, check if next is nullptr, return false if it is
"""
        