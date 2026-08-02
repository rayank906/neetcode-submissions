# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            0. if both empty, return None
            0b. if one is empty, return the other
            1. init head with the smallest, update ptrs accordingly
            2. while list1 and list2
            3. if list1.val < list2.val:
                init temp node to list1
                head.next = temp
                head = head.next
                list1 = list1.next
            4. else, repeat prev for list2
            5. while list1, add list1 nodes to head
            6. while list2, add list2 nodes to head ptr
            7. return head
        """
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = ListNode()
        if list1.val < list2.val:
            head.val = list1.val
            list1 = list1.next
        else:
            head.val = list2.val
            list2 = list2.next
        curr = head
        while list1 and list2:
            temp = ListNode()
            if list1.val < list2.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            curr.next = temp
            curr = curr.next
        while list1:
            temp = ListNode()
            temp.val = list1.val
            list1 = list1.next
            curr.next = temp
            curr = curr.next
        while list2:
            temp = ListNode()
            temp.val = list2.val
            list2 = list2.next
            curr.next = temp
            curr = curr.next
        return head
        