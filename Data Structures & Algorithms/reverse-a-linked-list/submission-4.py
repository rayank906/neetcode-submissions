# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            1. prev at null, curr and hold for next
            Idea is to reverse links one by one
            1b. while hold
            2. curr next assigned to prev
            3. move prev to curr, curr to hold and hold to hold next
            4. return curr
        """
        if not head:
            return None
        
        prev = None
        curr = head

        while curr:
            hold = curr.next
            curr.next = prev
            prev = curr
            curr = hold
        
        return prev


        