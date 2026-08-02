# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            """
               1. append root to stack
               2. curr = root
               3. while stack or curr
                    if curr is null:
                        stack.pop
                        self.res.append(cur.val)
                        cur = cur.right
                    else, append to stack and move left
            """
            n = 0
            stack = []
            curr = root

            while curr or stack:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    n += 1
                    if n == k:
                        return curr.val
                    curr = curr.right

"""
    1. make a global res array
    2. perform an inorder traversal using a helper function
    3. access kth - 1 element
    4. return that

    TimeC: O(n), traversing every node
    SpaceC: O(n), for resulting array
"""
        