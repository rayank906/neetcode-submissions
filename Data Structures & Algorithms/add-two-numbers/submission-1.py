# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        stack1 = []
        while curr:
            stack1.append(str(curr.val))
            curr = curr.next
        stack1.reverse()

        curr = l2
        stack2 = []
        while curr:
            stack2.append(str(curr.val))
            curr = curr.next
        stack2.reverse()

        resNum = str(int("".join(stack1)) + int("".join(stack2)))

        head = ListNode(int(resNum[-1]))
        prev = head
        for i in range(len(resNum) - 2, -1, -1):
            prev.next = ListNode(int(resNum[i]))
            prev = prev.next
        
        return head


"""
    1. loop through l1 and l2, adding elements to a stack
    2. change the reversed stacks to strings
    3. change each string to int and add them together
    4. loop by reverse through the resulting string and
    add the integers to nodes
    5. loop with prev and curr pointers to ensure the next links are made
    6. return head of new list
"""
        