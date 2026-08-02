# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            1. if not head, return head
            2. init prev, curr, temp to None, head, head
            3. while curr
            3b. temp = curr.next
            4. curr.next = prev
            5. prev = curr
            6. curr = temp
        """
        if not head:
            return None
        prev, curr, temp = None, head, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        