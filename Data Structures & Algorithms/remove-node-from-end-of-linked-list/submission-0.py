# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        if n == length:
            return head.next
        
        curr, prev = head, None
        for i in range(length - n):
            prev = curr
            curr = curr.next
        
        if prev == None:
            return None
        
        prev.next = curr.next
        curr.next = None

        return head

"""
    1. find length by looping once
    2. if n == len(arr):
        return head.next
    3. loop sz - n times w prev and curr
    4. if prev = None, return None
    5. else, prev.next = curr.next, curr.next = None
    6. return head 
"""