# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        
        dfs(root)

        return self.res[k - 1]

"""
    1. make a global res array
    2. perform an inorder traversal using a helper function
    3. access kth - 1 element
    4. return that

    TimeC: O(n), traversing every node
    SpaceC: O(n), for resulting array
"""
        