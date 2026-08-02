# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            1. init slow, fast ptr
            2. while slow.next and fast.next.next
            3. slow = slow.next, fast = fast.next.next
            4. if slow == fast:, return true
            5. return false
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        