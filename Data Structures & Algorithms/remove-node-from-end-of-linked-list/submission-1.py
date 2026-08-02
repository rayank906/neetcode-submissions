# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            0. loop once to find size
            1. loop with curr and prev, sending curr to size-nth node
            2. assign prev.next to curr.next
            3. return head

            Edge case: remove head, return head.next
        """
        if not head:
            return None
        
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1

        if (size - n) == 0:
            return head.next

        prev, curr = None, head
        i = 0
        while curr and i < (size - n):
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        return head
        