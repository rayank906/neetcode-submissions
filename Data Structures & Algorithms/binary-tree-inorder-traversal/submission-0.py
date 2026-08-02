# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res


        

"""
    Iterative solution:
    1. make a stack to simulate the call stack
    2. for every node, go as far left as we can, adding elems
    to the stack
    3. when we reach null, we want to pop from the stack and assign to curr
    4. append that popped elem to res
    5. go to the right

    TC: O(n), SC: O(n) for the stack and res array
"""
        